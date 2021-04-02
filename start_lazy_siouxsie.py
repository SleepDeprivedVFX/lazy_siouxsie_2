"""
GOALS:
1. Connect all of the other UI elements, Frame size, rate, aspect ratio
2. Create the Gray and Mirror Balls
3. Setup the quality and render settings
4. Setup the Deadline script
5. Get the lights layer working
"""
from __future__ import absolute_import
from __future__ import print_function
__author__ = 'Adam Benson'
__version__ = '2.0.0'

"""
1.0.1 Version Notes:
Bug fixes:

"""
print('Running Lazy Siouxsie v%s' % __version__)

import platform
import os
import sys
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.app.renderSetup.views.overrideUtils as utils
from maya import cmds
import glob
import re
from time import sleep
import math
from datetime import datetime
import json
import logging

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from PySide2 import QtCore, QtGui, QtWidgets
from ui.lazy_siouxsie_ui import Ui_lazySiouxsie
# sys.path.append(r'C:\Users\sleep\OneDrive\Documents\Scripts\Python\Maya\Lighting-Rendering_Utilities\lazy_siouxsie_2')
sys.path.append(sys.argv[0])

logger = logging.getLogger('LazySLog')


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system. 
    
    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("Lazy Siouxsie Auto Turntables...", app_instance, LazySiouxsie)


class LazySiouxsie(QtWidgets.QWidget):
    """
    Lazy Siouxsie's dialog box.
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtWidgets.QWidget.__init__(self)

        self.arnold_formate = {
            'png': 'png',
            'jpg': 'jpeg',
            'tif': 'tif',
            'mtoa_shaders': 'mtoa_shaders',
            'exr(deep)': 'deepexr',
            'exr': 'exr',
            'mplay': 'mplay',
            'maya': 'maya'
        }
        self.vray_formats = {
            'png': 'png',
            'jpg': 'jpg',
            'vrimg': 'vrimg',
            'hdr': 'hdr',
            'exr(singlepass)': 'exr',
            'exr': 'exr (multichannel)',
            'tga': 'tga',
            'bmp': 'bmp',
            'sgi': 'sgi',
            'tif': 'tif',
            'vrsm': 'vrsm',
            'vrst': 'vrst',
            'exr(deep)': 'exr(deep)'
        }
        self.light_types = [
            'aiAreaLight',
            'aiSkyDomeLight',
            'aiMeshLight',
            'aiPhotometricLight',
            'aiLightPortal',
            'aiPhysicalSky',
            'VRayGeoSun',
            'VRaySunShape',
            'VRaySunTarget',
            'VRayLightIESShape',
            'VRayLightRectShape',
            'VRayLightDomeShape',
            'VRayLightSphereShape'
        ]

        # Setup the UI
        self.ui = Ui_lazySiouxsie()
        self.ui.setupUi(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        # TODO: So, the self._app clearly has to be replaced since this needs to be engine proof
        #       For instance, FTrack won't work with Shotgun
        #       The self._app is doing 2 main things:
        #           1. It is getting configuration settings.  These can be moved to an internal config
        #               a. ls_config.cfg has been created for this purpose
        #           2. It is providing an engine from Shotgun for context and other data.
        # self._app = sgtk.platform.current_bundle()
        self._app = {
            'turntable_task': 'TNT_turntable',
            'output_format': 'PNG'
        }
        logger.info('Starting Lazy Siouxsie!')

        # Connect to Deadline
        os_sys = platform.system()
        self.computer = platform.node()
        if os_sys == 'Windows':
            # This should go into the paths.yml perhaps.  Setup a series of universal paths, and then call them here.
            python_path = 'C:\\Python27\\Lib\\site-packages'
        else:
            python_path = '/Volumes/Applications/Python27/Lib/site-packages'
        sys.path.append(python_path)
        # TODO: Check and make sure that the Deadline API is available, or move the dealine routine out of the main loop
        try:
            from Deadline import DeadlineConnect as connect
            deadline_connection = self._app.get_setting('deadline_connection')
            deadline_port = int(self._app.get_setting('deadline_port'))
            self.dl = connect.DeadlineCon(deadline_connection, deadline_port)
            logger.debug('Deadline Connection made!')
        except ImportError:
            self.dl = None
            logger.error('No Deadline to Python!')

        self.turntable_task = self._app['turntable_task']
        self.render_format = self._app['output_format']
        logger.debug('Collected Turntable Configuration Settings.')

        self.ground_plane = []
        self.scene_lights = None
        self.scene_selection = cmds.ls(sl=True)
        self.has_lights = self.check_scene_lights()
        logger.debug('Preforming Flight Precheck...')
        self.preflight_check = self.do_preflight_check()
        if not self.preflight_check:
            self.ui.spin_btn.setEnabled(False)
            self.ui.status_label.setStyleSheet('color: rgb(255, 0, 0);')
        logger.debug('Precheck complete.')

        # FIXME: The following is all the Shotgun connectivity and context stuff
        # engine = self._app.engine
        # self.sg = engine.sgtk
        # self.context = engine.context
        # self.project = self.context.project['name']
        # self.project_id = self.context.project['id']
        # self.entity = self.context.entity['type']
        # self.task = self.context.task['name']
        # self.entity_id = self.context.entity['id']
        # self.tt_task = None
        self.sg = None
        self.context = None
        self.project = None
        self.project_id = None
        self.entity = None
        self.task = None
        self.entity_id = None
        self.tt_task = None
        logger.debug('Shotgun context collected.')

        filters = [
            ['id', 'is', self.project_id]
        ]
        fields = [
            'sg_pixel_aspect',
            'sg_output_resolution',
            'sg_renderers'
        ]
        try:
            sg_settings = self.sg.shotgun.find_one('Project', filters, fields)

            sg_resolution = sg_settings['sg_output_resolution']
            split_res = sg_resolution.split('x')
            resolution_width = split_res[0]
            resolution_height = split_res[1]
            pixel_aspect = str(sg_settings['sg_pixel_aspect'])
            renderers = sg_settings['sg_renderers'][0]['name']
        except AttributeError:
            logger.error('Shit the bed on Shotgun')
            resolution_width = 1920
            resolution_height = 1080
            pixel_aspect = 1.0
            renderers = 'Arnold'
        finally:
            resolution_width = 1920
            resolution_height = 1080
            pixel_aspect = 1.0
            renderers = 'Arnold'

        if not pixel_aspect or pixel_aspect == 'None':
            pixel_aspect = '1.0'
        
        
        try:
            self.ui.res_width.setText(resolution_width)
            self.ui.res_height.setText(resolution_height)
            self.ui.pixel_aspect.setText(pixel_aspect)
            self.ui.rendering_engine.setCurrentText(renderers)
            hdri_path = self._app.get_setting('hdri_path')
            hdri_settings = self._app.get_setting('hdri_settings')
            logger.debug('Shotgun Render Settings Collected.')
        except TypeError:
            logger.error('Shit the bed on Render Settings')
            hdri_path = 'c:/sleep/'
            hdri_settings = 'None'

        if os.path.exists(hdri_path):
            print('PATH EXISTS')
            self.hdri_path = hdri_path
            files = os.listdir(hdri_path)
            for f in files:
                filepath = os.path.join(hdri_path, f)
                if os.path.isfile(filepath):
                    if f.endswith('.hdr') or f.endswith('.exr'):
                        hdri = QtGui.QListWidgetItem(f)
                        self.ui.hdriList.addItem(hdri)
                        self.ui.hdriList.setCurrentItem(hdri)
        if os.path.exists(hdri_settings):
            settings = open(hdri_settings, 'r')
            print('HDRI JSON About to load')
            self.hdri_setup = json.load(settings)
        else:
            self.hdri_setup = None
        file_to_send = cmds.file(q=True, sn=True)
        try:
            self.ui.file_path.setText(file_to_send)
            self.ui.file_path.setEnabled(False)
            self.ui.cancel_btn.clicked.connect(self.cancel)
            self.ui.spin_btn.clicked.connect(self.build_turn_table)
            self.ui.browse_btn.clicked.connect(self.browse)
            info = self.get_scene_details()
            self.ui.res_width.setText(info['width'])
            self.ui.res_height.setText(info['height'])
            self.ui.build_progress.setValue(0)
            self.ui.total_frames.setEnabled(False)
            self.ui.startFrame.valueChanged.connect(self.set_frames)
            self.ui.endFrame.valueChanged.connect(self.set_frames)
            self.ui.render_format.setCurrentText(self.render_format)
            self.ui.scene_lights.clicked.connect(self.scene_lights_checkbox)
            self.ui.full_circle.clicked.connect(self.set_range)
            self.ui.partial_circle.clicked.connect(self.set_range)
            self.ui.from_range.setEnabled(False)
            self.ui.to_range.setEnabled(False)
        except:
            pass
        logger.debug('Tool setup complete!')

    def set_frames(self):
        start = self.ui.startFrame.value()
        end = self.ui.endFrame.value()
        dif = (end - start) + 1
        total_frames = dif * 2
        self.ui.total_frames.setText(str(total_frames))

    def set_range(self):
        if self.ui.full_circle.isChecked():
            self.ui.from_range.setEnabled(False)
            self.ui.to_range.setEnabled(False)
        else:
            self.ui.from_range.setEnabled(True)
            self.ui.to_range.setEnabled(True)

    def cancel(self):
        self.close()

    def build_turn_table(self):
        # List tasks
        next_file = self.find_turntable_task()
        if next_file:
            self.ui.build_progress.setValue(1)
            self.ui.status_label.setText('Saving working file...')
            cmds.file(s=True)
            self.ui.build_progress.setValue(5)
            self.ui.status_label.setText('Saving Turntable file...')
            cmds.file(rn=next_file)
            cmds.file(s=True, type='mayaBinary')
            self.ui.build_progress.setValue(8)
            self.ui.status_label.setText('Getting HDRI Selections...')
            selected_hdri = self.get_hdri_files()

            # Temporarily hide all lights
            if self.scene_lights:
                cmds.hide(self.scene_lights)

            # Select and group the set
            self.ui.build_progress.setValue(10)
            self.ui.status_label.setText('Selecting scene geometry...')
            geo = cmds.ls(type=['mesh', 'nurbsSurface'])
            if self.ground_plane:
                for g in self.ground_plane:
                    if g in geo:
                        geo.remove(g)
                cmds.select(self.ground_plane, r=True)
                cmds.hide()
            cmds.select(geo, r=True)
            z = 1
            while z < 100:
                cmds.pickWalk(d='up')
                z += 1
            self.ui.build_progress.setValue(12)
            self.ui.status_label.setText('Grouping the geometry...')
            group = cmds.group(n='_Turntable_Set_Prep')

            # Setup the camera bit
            self.ui.build_progress.setValue(14)
            self.ui.status_label.setText('Building the Turntable Camera...')
            start = self.ui.startFrame.value()
            end = self.ui.endFrame.value()
            camera_data = self.build_camera(start=start, end=end, group=group)
            camera = camera_data[0]
            center = camera_data[1]
            bb = camera_data[2]
            scene_max_width = camera_data[3]
            x_min = bb[0]
            y_min = bb[1]
            z_min = bb[2]
            x_max = bb[3]
            y_max = bb[4]
            z_max = bb[5]

            self.ui.build_progress.setValue(34)
            self.ui.status_label.setText('Set frame ranges...')
            total_frames = int(self.ui.total_frames.text())
            add_frames = total_frames/2
            extended_end = end + add_frames
            cmds.playbackOptions(min=start, max=extended_end)
            # Get the rendering engine
            self.ui.build_progress.setValue(35)
            self.ui.status_label.setText('Get the rendering engine...')
            rendering_engine = self.ui.rendering_engine.currentText()
            lights = self.ui.scene_lights.isChecked()

            # This will need some major renumbering
            self.ui.build_progress.setValue(36)
            self.ui.status_label.setText('Get scene lighting requirements...')
            # Restore lights
            if self.scene_lights:
                cmds.showHidden(self.scene_lights)

            use_scene_lighting = self.ui.scene_lights.isChecked()
            if use_scene_lighting and self.has_lights:
                self.ui.build_progress.setValue(37)
                self.ui.status_label.setText('Get Scene Lights...')
                get_scene_lights = self.get_scene_lights(renderer=rendering_engine, group=group, center=center)
                self.animate_dome(trans=get_scene_lights[1], start=end, end=extended_end)
            elif not use_scene_lighting and self.has_lights:
                self.ui.build_progress.setValue(37)
                self.ui.status_label.setText('Packing Artist Lights...')
                get_scene_lights = self.get_scene_lights(renderer=rendering_engine, group=group, center=center)
            else:
                self.ui.build_progress.setValue(37)
                self.ui.status_label.setText('Ignoring scene lights...')
                # Once this is rewritten, this should = None
                get_scene_lights = [[], '']

            self.ui.build_progress.setValue(40)
            self.ui.status_label.setText('Build HDRI dome...')
            hdri_dome = self.build_hdri_dome(renderer=rendering_engine, lights=lights, hdri_list=selected_hdri,
                                             center=center)
            dome = hdri_dome['dome']
            file_node = hdri_dome['file']
            light_trans = hdri_dome['translation']

            self.ui.build_progress.setValue(50)
            self.ui.status_label.setText('Animating the HDRI dome...')
            self.animate_dome(trans=light_trans, start=end, end=extended_end)

            self.ui.build_progress.setValue(51)
            self.ui.status_label.setText('Check groundplane setting...')
            # Reset the artists ground plane
            if self.ground_plane:
                cmds.select(self.ground_plane, r=True)
                cmds.showHidden(self.ground_plane)
            # Check for the auto-ground plane
            ground = self.ui.ground_plane.isChecked()
            ground_plane = None
            if ground:
                self.ui.build_progress.setValue(52)
                self.ui.status_label.setText('Building Ground Plane...')
                radius = 10 * scene_max_width
                if cmds.about(q=True, v=True) < '2018':
                    ground_plane = cmds.polyPlane(h=radius, w=radius, ax=[0, 1, 0], ch=True, cuv=2,
                                                  n='_turntable_ground_plane', sx=10, sy=20)
                    cmds.delete(ch=True)
                    self.texture_ground(ground=ground_plane, renderer=rendering_engine, file_node=hdri_dome['file'])
                else:
                    cmds.polyDisc(s=4, sm=4, sd=3, r=radius)
                    cmds.rename('_turntable_ground_plane')
                    cmds.delete(ch=True)
                    ground_plane = cmds.ls(sl=True)[0]
                    self.texture_ground(ground=ground_plane, renderer=rendering_engine, file_node=hdri_dome['file'])
                self.ui.build_progress.setValue(54)
                self.ui.status_label.setText('Set the plane Position...')
                cmds.select(ground_plane, r=True)
                cmds.setAttr('%s.tx' % ground_plane, center[0])
                cmds.setAttr('%s.ty' % ground_plane, y_min)
                cmds.setAttr('%s.tz' % ground_plane, center[2])
                cmds.addAttr(ground_plane, ln='original_file', dt='string')
                original_file = os.path.basename(self.ui.file_path.text())
                cmds.setAttr('%s.original_file' % ground_plane, original_file, type='string')
                self.ground_plane.append(ground_plane)

            self.ui.build_progress.setValue(55)
            self.ui.status_label.setText('Checking for Chrome Sphere creation...')
            get_spheres = self.ui.chrome_balls.isChecked()
            spheres = []
            if get_spheres:
                # TODO: Need to refigure out how and where to put the chrome balls.  Check Tiger for example
                self.ui.build_progress.setValue(56)
                self.ui.status_label.setText('Finding Radius...')
                # base_max_width = math.sqrt((math.pow((x_max - x_min), 2)) + (math.pow((y_max - y_min), 2)))
                base_max_width = scene_max_width
                sphere_radius = ((y_max - y_min)/2) * 0.25
                self.ui.build_progress.setValue(58)
                self.ui.status_label.setText('Making sphers...')
                chrome_ball = cmds.polySphere(r=sphere_radius, n='_turntable_chrome_ball')
                gray_ball = cmds.polySphere(r=sphere_radius, n='_turntable_gray_ball')
                cmds.addAttr(chrome_ball, ln='original_file', dt='string')
                original_file = os.path.basename(self.ui.file_path.text())
                cmds.setAttr('%s.original_file' % chrome_ball[0], original_file, type='string')
                cmds.addAttr(gray_ball, ln='original_file', dt='string')
                cmds.setAttr('%s.original_file' % gray_ball[0], original_file, type='string')

                self.ui.build_progress.setValue(60)
                self.ui.status_label.setText('Positioning Spheres...')
                # positioning of the chrome balls
                chrome_x_point = center[0] + ((base_max_width / 2) * .85)
                gray_x_point = chrome_x_point + (sphere_radius * 2.2)
                sphere_ground = y_min + sphere_radius
                cmds.setAttr('%s.tx' % chrome_ball[0], chrome_x_point)
                cmds.setAttr('%s.ty' % chrome_ball[0], sphere_ground)
                cmds.setAttr('%s.tz' % chrome_ball[0], center[2])
                cmds.setAttr('%s.tx' % gray_ball[0], gray_x_point)
                cmds.setAttr('%s.ty' % gray_ball[0], sphere_ground)
                cmds.setAttr('%s.tz' % gray_ball[0], center[2])
                spheres.append(chrome_ball)
                spheres.append(gray_ball)
                materials = self.texture_chrome_balls(spheres=spheres, renderer=rendering_engine)

            self.ui.build_progress.setValue(62)
            self.ui.status_label.setText('Begin Layers Setup...')
            layers = self.setup_render_layers(dome=dome, file_node=file_node, ground=self.ground_plane,
                                              light_trans=light_trans, hdri_list=selected_hdri, cam=camera,
                                              lights=get_scene_lights[0], light_grp=get_scene_lights[1],  balls=spheres)

            self.ui.build_progress.setValue(68)
            self.ui.status_label.setText('Setting render settings...')
            # Setup the rendering setup
            self.setup_rendering_engine(renderer=rendering_engine, render_format=self.render_format,
                                        task=self.turntable_task, filename=next_file, cam=camera)
            # Send to the farm.
            send_to_deadline = self.ui.submit_to_deadline.isChecked()
            if send_to_deadline:
                self.ui.build_progress.setValue(76)
                self.ui.status_label.setText('Creating Deadline Job...')
                self.submit_to_deadline(start=start, end=extended_end, renderer=rendering_engine, camera=camera,
                                        layers=layers)

            # Finalizing
            self.ui.build_progress.setValue(96)
            self.ui.status_label.setText('Saving Turntable file...')
            cmds.file(s=True)
            if self.ui.open_turntable.isChecked():
                self.ui.build_progress.setValue(100)
                self.ui.status_label.setText('Done!')
            else:
                self.ui.build_progress.setValue(99)
                self.ui.status_label.setText('Reopening the main file...')
                file_to_return = self.ui.file_path.text()
                cmds.file(file_to_return, o=True)
                self.ui.build_progress.setValue(100)
                self.ui.status_label.setText('Done!')
            sleep(3)
            self.cancel()
            if self.scene_selection:
                cmds.select(self.scene_selection, r=True)

    def texture_ground(self, ground=None, renderer=None, file_node=None):
        if ground:
            self.ui.build_progress.setValue(53)
            self.ui.status_label.setText('Textureing the ground...')
            if renderer == 'arnold':
                material = cmds.shadingNode('aiShadowMatte', asShader=True, n='_turntable_ground_mat')
                cmds.select(ground, r=True)
                cmds.hyperShade(a=material)
            elif renderer == 'vray':
                material = cmds.shadingNode('VRayMtlWrapper', asShader=True, n='_turntable_ground_mat')
                vray_base_mat = cmds.shadingNode('VRayMtl', asShader=True, n='_turntable_vray_ground_base')
                cmds.connectAttr('%s.outColor' % vray_base_mat, '%s.baseMaterial' % material, f=True)
                cmds.connectAttr('%s.outColor' % file_node, '%s.color' % vray_base_mat, f=True)
                cmds.select(ground, r=True)
                cmds.hyperShade(a=material)
                cmds.setAttr('%s.matteSurface' % material, 1)
                cmds.setAttr('%s.shadows' % material, 1)
                cmds.setAttr('%s.affectAlpha' % material, 1)
                cmds.setAttr('%s.alphaContribution' % material, -1)
                cmds.setAttr('vraySettings.giOn', 0)
                cmds.setAttr('vraySettings.cam_overrideEnvtex', 1)
                cmds.connectAttr('%s.outColor' % file_node, 'vraySettings.cam_envtexBg', f=True)

    def setup_rendering_engine(self, renderer=None, render_format=None, task=None, filename=None, cam=None):
        if renderer:
            self.ui.build_progress.setValue(69)
            self.ui.status_label.setText('Getting UI and scene render settings...')
            split_path = filename.rsplit('.', 1)[0]
            version = split_path.rsplit('_', 1)[1]
            pixel_aspect = self.ui.pixel_aspect.text()
            resolutionWidth = int(self.ui.res_width.text())
            resolutionHeight = int(self.ui.res_height.text())
            resolution_scale = self.ui.res_scale.currentText()
            start_frame = float(self.ui.startFrame.text())
            end_frame = float(self.ui.endFrame.text())
            quality = self.ui.quality_value.value()
            resolution_scale = float(resolution_scale.strip('%'))
            resolution_scale /= 100
            resolutionHeight *= resolution_scale
            resolutionWidth *= resolution_scale

            if renderer == 'vray':
                self.ui.build_progress.setValue(69)
                self.ui.status_label.setText('Creating VRay settings...')
                cmds.setAttr('vraySettings.aspectLock', 0)
                cmds.setAttr('vraySettings.animType', 1)
                cmds.setAttr('defaultRenderGlobals.startFrame', start_frame)
                cmds.setAttr('defaultRenderGlobals.endFrame', end_frame)
                self.ui.build_progress.setValue(70)
                self.ui.status_label.setText('Checking plugins...')
                if not cmds.pluginInfo('vrayformaya', q=True, l=True):
                    try:
                        cmds.loadPlugin('vrayformaya')
                    except:
                        print('CANNOT LOAD V-RAY')

                self.ui.build_progress.setValue(71)
                self.ui.status_label.setText('Setting engine...')
                cmds.setAttr('defaultRenderGlobals.ren', renderer, type='string')

                self.ui.build_progress.setValue(72)
                self.ui.status_label.setText('Creating render string...')
                pathSettings = '%s/<layer>/%s/<layer>_<scene>' % (task, version)
                cmds.setAttr('vraySettings.fileNamePrefix', pathSettings, type='string')

                self.ui.build_progress.setValue(73)
                self.ui.status_label.setText('Setting up frame sizes and image format...')
                cmds.setAttr('vraySettings.width', int(resolutionWidth))
                cmds.setAttr('vraySettings.height', int(resolutionHeight))
                print('pixel_aspect: %s' % pixel_aspect)
                cmds.setAttr('vraySettings.pixelAspect', float(pixel_aspect))

                output = render_format.lower()
                cmds.setAttr('vraySettings.imageFormatStr', self.vray_formats[output], type='string')

                self.ui.build_progress.setValue(74)
                self.ui.status_label.setText('Calculating quality settings...')
                dmc_maxSubDivs = int(2.4 * quality)
                dmc_threshold = 0.1 / quality
                # Adaptive Amount base on the following equation with constants figured out from domain and range
                # variables
                # d = Adaptive Amplitude
                # r = Adaptive Slope
                # f(x) = d * arctan(r * x) - 1.05
                adaptive_amplitude = 1.35950130973274
                adaptive_slope = 0.99
                adaptive_amount = adaptive_amplitude * math.atan(adaptive_slope * float(quality)) - 1.05
                # Adaptive Threshold based on the following equation with constants figured out from domain/range
                # variables
                # d = Threshold Amplitude
                # f(x) = -d * arctan(x) + 0.195
                threshold_amplitude = 0.12915262442461
                adaptive_threshold = ((-1 * threshold_amplitude) * math.atan(float(quality))) + 0.195

                self.ui.build_progress.setValue(75)
                self.ui.status_label.setText('Setting render quality...')
                cmds.setAttr('vraySettings.samplerType', 4)
                cmds.setAttr('vraySettings.minShadeRate', quality)
                cmds.setAttr('vraySettings.giOn', 0)
                cmds.setAttr('vraySettings.cam_overrideEnvtex', 1)
                cmds.setAttr('vraySettings.dmcMinSubdivs', 1)
                cmds.setAttr('vraySettings.dmcMaxSubdivs', dmc_maxSubDivs)
                cmds.setAttr('vraySettings.dmcThreshold', dmc_threshold)
                cmds.setAttr('vraySettings.dmcs_adaptiveAmount', adaptive_amount)
                cmds.setAttr('vraySettings.dmcs_adaptiveThreshold', adaptive_threshold)

            elif renderer == 'arnold':
                self.ui.build_progress.setValue(69)
                self.ui.status_label.setText('Checking plugins...')
                if not cmds.pluginInfo('mtoa', q=True, l=True):
                    try:
                        cmds.loadPlugin('mtoa')
                    except:
                        print('CANNOT LOAD ARNOLD!')
                self.ui.build_progress.setValue(71)
                self.ui.status_label.setText('Setting engine and output path...')
                pathSettings = '%s/<RenderLayer>/%s/<RenderLayer>_<Scene>' % (task, version)

                cmds.setAttr('defaultRenderGlobals.ren', renderer, type='string')
                self.ui.build_progress.setValue(72)
                self.ui.status_label.setText('Setting up frame range and output settings...')
                cmds.setAttr('defaultRenderGlobals.imageFilePrefix', pathSettings, type='string')
                cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
                cmds.setAttr('defaultRenderGlobals.animation', 1)
                cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
                cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
                cmds.setAttr('defaultRenderGlobals.startFrame', start_frame)
                cmds.setAttr('defaultRenderGlobals.endFrame', end_frame)

                self.ui.build_progress.setValue(73)
                self.ui.status_label.setText('Setting resolution and file format...')
                cmds.setAttr('defaultResolution.width', resolutionWidth)
                cmds.setAttr('defaultResolution.height', resolutionHeight)

                output = render_format.lower()
                cmds.setAttr('defaultArnoldDriver.ai_translator', self.arnold_formate[output], type='string')

                self.ui.build_progress.setValue(74)
                self.ui.status_label.setText('Calculating quality settings...')
                quality_mult = 0.4
                secondary_samples = int(math.ceil(quality * quality_mult))
                self.ui.build_progress.setValue(75)
                self.ui.status_label.setText('Setting rendering quality...')
                cmds.setAttr('defaultArnoldRenderOptions.AASamples', quality)
                cmds.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', secondary_samples)
                cmds.setAttr('defaultArnoldRenderOptions.GISpecularSamples', secondary_samples)
                cmds.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', secondary_samples)
                cmds.setAttr('defaultArnoldRenderOptions.GISssSamples', secondary_samples)
                cmds.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', (secondary_samples - 1))

    def texture_chrome_balls(self, spheres=None, renderer=None):
        materials = {}
        if spheres:
            chrome_transform = spheres[0][0]
            chrome_shape = spheres[0][1]
            gray_transform = spheres[1][0]
            gray_shape = spheres[1][1]
            if renderer == 'arnold':
                gray_surface = cmds.shadingNode('aiStandardSurface', asShader=True, n='_turntable_gray_mat')
                chrome_surface = cmds.shadingNode('aiStandardSurface', asShader=True, n='_turntable_chrome_mat')
                cmds.select(chrome_transform, r=True)
                cmds.hyperShade(a=chrome_surface)
                cmds.select(gray_transform, r=True)
                cmds.hyperShade(a=gray_surface)

                cmds.setAttr('%s.metalness' % chrome_surface, 1)
                cmds.setAttr('%s.base' % chrome_surface, 1)
                cmds.setAttr('%s.baseColor' % chrome_surface, 1, 1, 1, type='double3')
                cmds.setAttr('%s.specular' % chrome_surface, 0)
                cmds.setAttr('%s.specularAnisotropy' % chrome_surface, 0.5)

                cmds.setAttr('%s.base' % gray_surface, 1)
                cmds.setAttr('%s.baseColor' % gray_surface, 0.5, 0.5, 0.5, type='double3')
                cmds.setAttr('%s.specularColor' % gray_surface, 0.5, 0.5, 0.5, type='double3')
                cmds.setAttr('%s.specular' % gray_surface, 1)
                cmds.setAttr('%s.specularRoughness' % gray_surface, 0.65)

            elif renderer == 'vray':
                gray_surface = cmds.shadingNode('VRayMtl', asShader=True, n='_turntable_gray_mat')
                chrome_surface = cmds.shadingNode('VRayMtl', asShader=True, n='_turntable_chrome_mat')
                cmds.select(chrome_transform, r=True)
                cmds.hyperShade(a=chrome_surface)
                cmds.select(gray_transform, r=True)
                cmds.hyperShade(a=gray_surface)

                cmds.setAttr('%s.useFresnel' % chrome_surface, 0)
                cmds.setAttr('%s.reflectionColor' % chrome_surface, 1, 1, 1, type='double3')
                cmds.setAttr('%s.diffuseColorAmount' % chrome_surface, 0)
                cmds.setAttr('%s.color' % chrome_surface, 1, 1, 1, type='double3')

                cmds.setAttr('%s.color' % gray_surface, 0.5, 0.5, 0.5, type='double3')
                cmds.setAttr('%s.reflectionColor' % gray_surface, 0.5, 0.5, 0.5, type='double3')
                cmds.setAttr('%s.hilightGlossinessLock' % gray_surface, 0)
                cmds.setAttr('%s.reflectionGlossiness' % gray_surface, 0)
                cmds.setAttr('%s.hilightGlossiness' % gray_surface, 0.35)
            elif renderer == 'renderman':
                pass
            elif renderer == 'redshift':
                pass
            else:
                gray_surface = cmds.shadingNode('blinn', asShader=True, n='_turntable_gray_mat')
                chrome_surface = cmds.shadingNode('blinn', asShader=True, n='_turntable_chrome_mat')
                cmds.select(chrome_transform, r=True)
                cmds.hyperShade(a=chrome_surface)
                cmds.select(gray_transform, r=True)
                cmds.hyperShade(a=gray_surface)

            materials['gray_shader'] = gray_surface
            materials['chrome_shader'] = chrome_surface

        return materials

    def build_hdri_dome(self, renderer=None, lights=None, hdri_list=None, center=None):
        hdri = {}
        if renderer == 'arnold':
            self.ui.build_progress.setValue(41)
            self.ui.status_label.setText('Create Arnold SkyDome...')
            light = cmds.createNode('aiSkyDomeLight')
            self.ui.build_progress.setValue(42)
            self.ui.status_label.setText('Get parent translation...')
            cmds.pickWalk(d='up')
            cmds.rename('_HDRI_light')
            light_trans = cmds.ls(sl=True)[0]
            self.ui.build_progress.setValue(44)
            self.ui.status_label.setText('Connect Light to file...')
            cmds.connectAttr('%s.instObjGroups' % light_trans, 'defaultLightSet.dagSetMembers', na=True)
            file_node = cmds.createNode('file')
            cmds.connectAttr('%s.outColor' % file_node, '%s.color' % light, f=True)
            hdri['dome'] = light
            hdri['file'] = file_node
            hdri['translation'] = light_trans
        elif renderer == 'vray':
            self.ui.build_progress.setValue(46)
            self.ui.status_label.setText('Create VRay Dome Light...')
            light = cmds.createNode('VRayLightDomeShape', n='_HDRI_lightShape')
            self.ui.build_progress.setValue(47)
            self.ui.status_label.setText('Get parent translation...')
            cmds.pickWalk(d='up')
            cmds.rename('_HDRI_light')
            light_trans = cmds.ls(sl=True)[0]
            self.ui.build_progress.setValue(48)
            self.ui.status_label.setText('Connect Light to file...')
            cmds.setAttr('%s.useDomeTex' % light, 1)
            file_node = cmds.createNode('file')
            cmds.connectAttr('%s.outColor' % file_node, '%s.domeTex' % light, f=True)

            vray_shit = cmds.createNode('VRayPlaceEnvTex', n='vray_placement')
            cmds.connectAttr('%s.outUV' % vray_shit, '%s.uvCoord' % file_node, f=True)
            cmds.setAttr('%s.useTransform' % vray_shit, 1)
            cmds.setAttr('%s.mappingType' % vray_shit, 2)
            vray_sucks = cmds.createNode('place2dTexture', n='because_fucking_vray')
            cmds.connectAttr('%s.uvCoord' % vray_sucks, '%s.outUV' % vray_shit, f=True)

            hdri['dome'] = light
            hdri['file'] = file_node
            hdri['translation'] = light_trans
        elif renderer == 'redshift':
            # Figure out RedShift code
            pass
        elif renderer == 'renderman':
            # Figure out RedShift code
            pass
        elif renderer == 'mayasoftware':
            pass
        cmds.select(light_trans, r=True)
        cmds.xform(t=center, ws=True)
        cmds.addAttr(light_trans, ln='original_file', dt='string')
        original_file = os.path.basename(self.ui.file_path.text())
        cmds.setAttr('%s.original_file' % light_trans, original_file, type='string')
        return hdri

    def get_hdri_files(self):
        hdri_files = []
        files_list = self.ui.hdriList.selectedItems()
        self.ui.build_progress.setValue(9)
        self.ui.status_label.setText('Collecting HDRIs...')
        if files_list:
            for hdri in files_list:
                hdri_files.append(self.hdri_path + '/' + hdri.text())
        if self.ui.custom_hdri.text():
            hdri_files.append(self.ui.custom_hdri.text())
        return hdri_files

    def setup_render_layers(self, dome=None, file_node=None, ground=[], light_trans=None, hdri_list=None, cam=None,
                            lights=[], light_grp=None, balls=[]):
        layers = []
        self.ui.build_progress.setValue(63)
        self.ui.status_label.setText('Setting up render layers...')
        renderer = self.ui.rendering_engine.currentText()
        rs = renderSetup.instance()
        default_render_layer = rs.getDefaultRenderLayer()
        default_render_layer.setRenderable(False)
        # lights = list(lights)

        new_ground = []
        if self.ground_plane:
            for g in self.ground_plane:
                if cmds.nodeType(g) != 'transform':
                    find_trans = cmds.listRelatives(g, p=True)
                    for trans in find_trans:
                        if cmds.nodeType(trans) == 'transform':
                            new_ground.append(trans)
                            break
                else:
                    new_ground.append(g)
            ground_list = ', '.join(new_ground)
        else:
            ground_list = ''

        self.ui.build_progress.setValue(64)
        self.ui.status_label.setText('Collecting Turntable Geo...')
        chrome_balls = ''
        if balls:
            self.ui.build_progress.setValue(65)
            self.ui.status_label.setText('Adding spheres...')
            for ball in balls:
                chrome_balls = '%s, %s' % (chrome_balls, ball[0])
        if hdri_list:
            self.ui.build_progress.setValue(66)
            self.ui.status_label.setText('Creating render layers...')
            for hdri in hdri_list:
                # Get the basic filename for the render layer name
                basename = os.path.basename(hdri)
                base = os.path.splitext(basename)[0]
                render_layer = rs.createRenderLayer(base)
                layers.append(base)
                collection_set = render_layer.createCollection('Scene_%s' % base)
                collection_set.getSelector().setPattern('_Turntable_Set_Prep, %s, %s' %
                                                        (chrome_balls, ground_list))
                rs.switchToLayer(render_layer)
                utils.createAbsoluteOverride(file_node, 'fileTextureName')
                cmds.setAttr('%s.fileTextureName' % file_node, hdri, type='string')
                if self.hdri_setup:
                    extra_settings = self.hdri_setup[basename]
                    settings = extra_settings[renderer]
                    for setting in settings:
                        node = setting['node']
                        if node == 'light':
                            utils.createAbsoluteOverride(dome, setting['setting'])
                            if setting['type']:
                                cmds.setAttr('%s.%s' % (dome, setting['setting']), setting['value'],
                                             type=setting['type'])
                            else:
                                cmds.setAttr('%s.%s' % (dome, setting['setting']), setting['value'])
                        elif node == 'file':
                            utils.createAbsoluteOverride(file_node, setting['setting'])
                            if setting['type']:
                                cmds.setAttr('%s.%s' % (file_node, setting['setting']), setting['value'],
                                             type=setting['type'])
                            else:
                                cmds.setAttr('%s.%s' % (file_node, setting['setting']), setting['value'])
                        elif node == 'camera':
                            utils.createAbsoluteOverride(cam[1], setting['setting'])
                            if setting['type']:
                                cmds.setAttr('%s.%s' % (cam[1], setting['setting']), setting['value'],
                                             type=setting['type'])
                            else:
                                cmds.setAttr('%s.%s' % (cam[1], setting['setting']), setting['value'])

                if lights:
                    utils.createAbsoluteOverride(light_trans, 'visibility')
                    cmds.select(light_trans, r=True)
                    cmds.setAttr('%s.visibility' % light_trans, 1)
                    utils.createAbsoluteOverride(light_grp, 'visibility')
                    cmds.select(light_grp, r=True)
                    cmds.setAttr('%s.visibility' % light_grp, 0)

        if lights and self.ui.scene_lights.isChecked():
            render_layer = rs.createRenderLayer('Artist_Lights')
            collection_set = render_layer.createCollection('geo')
            collection_set.getSelector().setPattern('_Turntable_Set_Prep, %s, %s' % (chrome_balls, ground_list))
            light_collection = render_layer.createCollection('artist_lights')
            light_list = ''
            for light in lights:
                light_list += '%s, ' % light
            light_collection.getSelector().setPattern(light_list)
            rs.switchToLayer(render_layer)
            utils.createAbsoluteOverride(light_trans, 'visibility')
            cmds.setAttr('%s.visibility' % light_trans, 0)
            utils.createAbsoluteOverride(light_grp, 'visibility')
            cmds.select(light_grp, r=True)
            cmds.setAttr('%s.visibility' % light_grp, 1)
        elif lights and not self.ui.scene_lights.isChecked():
            cmds.select(light_grp, r=True)
            cmds.setAttr('%s.visibility' % light_grp, 0)

        rs.switchToLayer(None)
        return layers

    def check_scene_lights(self):
        lights = []
        light_types = self.light_types
        for light in light_types:
            type_list = cmds.ls(type=light)
            for t in type_list:
                lights.append(t)
        maya_light_types = cmds.ls(lights=True)
        for light in maya_light_types:
            lights.append(light)
        if lights:
            self.ui.scene_lights.setChecked(True)
            self.ui.status_label.setText('Lights in the Scene!')
            logger.info('This scene has lights in it.  Use Scene Lights has been turned on.')
            self.scene_lights = lights
            self.ui.build_progress.setValue(0)
            return True
        self.ui.scene_lights.setChecked(False)
        self.ui.status_label.setText('No lights found in scene')
        self.ui.build_progress.setValue(0)
        return False

    def scene_lights_checkbox(self):
        if not self.has_lights:
            self.ui.scene_lights.setChecked(False)

    def get_scene_lights(self, renderer=None, group=None, center=None):
        logger.debug('Begin packing scene lights.')
        lights = []
        self.ui.build_progress.setValue(38)
        self.ui.status_label.setText('Getting Lights...')
        light_types = self.light_types

        logger.debug('Checking for known light types...')
        for light in light_types:
            type_list = cmds.ls(type=light)
            for t in type_list:
                lights.append(t)

        self.ui.build_progress.setValue(39)
        self.ui.status_label.setText('getting Maya Lights...')
        for light in cmds.ls(lt=True):
            lights.append(light)

        logger.debug('Lights collected.')
        light_roots = []
        if lights:
            logger.debug('Parsing lights.')
            for light in lights:
                cmds.select(light, r=True)
                i = 0
                while i < 100:
                    cmds.pickWalk(d='up')
                    i += 1
                if cmds.ls(sl=True)[0] not in light_roots:
                    light_roots.append(cmds.ls(sl=True)[0])
            for root in light_roots:
                if root == group:
                    light_roots.remove(root)
            cmds.select(light_roots, r=True)
        if lights:
            logger.debug('Grouping Lights...')
            light_group = cmds.group(n='_turntable_light_group')
        else:
            light_group = None
        if center and light_group:
            logger.debug('Centering light group pivot')
            cmds.select(light_group, r=True)
            cmds.xform(piv=center, ws=True)
        return [lights, light_group]

    def browse(self):
        finder = QtGui.QFileDialog.getOpenFileName(self, filter='HDRI (*.hdr *.exr)')
        if finder:
            logger.debug('Returning Custom HDRI: %s' % finder[0])
            self.ui.custom_hdri.setText(finder[0])

    def get_scene_details(self):
        logger.debug('Getting scene details from Shotgun...')
        filters = [
            ['name', 'is', self.project]
        ]
        fields = ['sg_renderers', 'sg_output_resolution', 'sg_frame_rate', 'sg_render_format', 'sg_pixel_aspect']
        try:
            projectInfo = self.sg.shotgun.find_one("Project", filters, fields)
            info = {}
            resolution = projectInfo['sg_output_resolution']
            info['width'] = resolution.split('x')[0]
            info['height'] = resolution.split('x')[1]
            info['frame_rate'] = projectInfo['sg_frame_rate']
            info['render_format'] = projectInfo['sg_render_format']['name']
            info['render_engine'] = projectInfo['sg_renderers'][0]['name']
            info['aspect_ratio'] = projectInfo['sg_pixel_aspect']
        except AttributeError:
            return None
        return info

    def find_turntable_task(self):
        logger.info('Collecting Turntable file name from Shotgun and System...')
        filters = [
            ['entity', 'is', {'type': 'Asset', 'id': self.entity_id}]
        ]
        fields = ['content']
        tasks = self.sg.shotgun.find('Task', filters, fields)
        self.ui.build_progress.setValue(1)
        self.ui.status_label.setText('Getting Shotgun Tasks...')
        template = self.sg.templates['asset_work_area_maya']
        this_file = self.ui.file_path.text()
        path = os.path.dirname(this_file)
        # path = path.split('assets')[1]
        # path = 'assets' + path
        path = path.replace('\\', '/')
        settings = template.get_fields(path)
        for task in tasks:
            content = task['content']
            task_id = task['id']
            if content == self.turntable_task:
                turntable = content
                turntable_id = task_id
                self.tt_task = task_id
                break
            else:
                turntable = None
                turntable_id = None
        tt_path = path.replace(settings['task_name'], self.turntable_task)
        self.ui.build_progress.setValue(3)
        self.ui.status_label.setText('Turntable path: %s' % tt_path)
        logger.debug('Find version number...')
        version_pattern = r'(_v\d*|_V\d*)'
        if turntable:
            # Find latest turntable task
            logger.debug('Turntable task already exists!')
            if os.path.isdir(tt_path):
                files = glob.glob('%s/*[0-9]*' % tt_path)
                if files:
                    files.sort()
                    last_file = files[-1]
                    basename = os.path.basename(last_file)
                    version_string = re.search(version_pattern, basename)
                    last_version = version_string.group().lower()
                    version_number = last_version.strip('_v')
                    version_count = len(version_number)
                    version_number = int(version_number)
                    next_version = version_number + 1
                    version_number = str('{n:0{l}d}'.format(n=version_number, l=version_count))
                    next_version_number = str('{n:0{l}d}'.format(n=next_version, l=version_count))
                    version = last_version.replace(version_number, next_version_number)
                    next_file = last_file.replace(last_version, version)
                    logger.debug('Next filename created!  %s' % next_file)
                else:
                    next_file = '%s/%s_%s_v001.mb' % (tt_path, settings['Asset'], self.turntable_task)
                    logger.debug('First filename created!  %s' % next_file)
            else:
                os.makedirs(tt_path)
                next_file = '%s/%s_%s_v001.mb' % (tt_path, settings['Asset'], self.turntable_task)
                logger.debug('First filename and folder structure created!  %s' % next_file)
        else:
            # Create Turntable Task
            logger.info('Creating initial turntable task on Shotgun...')
            filters = [
                ['code', 'is', 'Turntable']
            ]
            fields = ['id']
            step = self.sg.shotgun.find_one('Step', filters, fields)
            task_data = {
                'project': {'type': 'Project', 'id': self.project_id},
                'entity': {'type': 'Asset', 'id': self.entity_id},
                'content': self.turntable_task,
                'step': {'type': 'Step', 'id': step['id']},
            }
            new_task = self.sg.shotgun.create('Task', task_data)
            self.tt_task = new_task['id']
            logger.debug('Task created!: %s' % new_task)
            if not os.path.isdir(tt_path):
                os.makedirs(tt_path)
                next_file = '%s/%s_%s_v001.mb' % (tt_path, settings['Asset'], self.turntable_task)
                logger.debug('Task set on Shotgun and new filename and folder structure created! %s' % next_file)
        self.ui.build_progress.setValue(4)
        self.ui.status_label.setText('New Filename: %s' % next_file)
        logger.info('New Filename: %s' % next_file)
        return next_file

    def build_camera(self, start=1, end=120, group=None):
        # Get the set/scene size from the bounding box
        logger.info('Building the camera system...')
        cmds.select(group, r=True)
        self.ui.build_progress.setValue(16)
        self.ui.status_label.setText('Getting scene center point...')
        logger.debug('Getting scene center point...')
        scene_bb = cmds.xform(q=True, bb=True)
        # Find the center from the bounding box
        x_center = scene_bb[3] - ((scene_bb[3] - scene_bb[0]) / 2)
        y_center = scene_bb[4] - ((scene_bb[4] - scene_bb[1]) / 2)
        z_center = scene_bb[5] - ((scene_bb[5] - scene_bb[2]) / 2)
        self.ui.build_progress.setValue(18)
        self.ui.status_label.setText('Animating the Set...')
        logger.debug('Animating the set...')
        cmds.select(group, r=True)
        bb_center = [x_center, y_center, z_center]
        cmds.xform(piv=[x_center, y_center, z_center])
        self.animate_dome(trans=group, start=start, end=end)
        # calculate a new height for the camera based on the bounding box
        logger.debug('Calculating camera height from bounding box...')
        user_cam_height = self.ui.camera_height.text()
        if user_cam_height != '':
            cam_height = float(user_cam_height) + scene_bb[1]
        else:
            cam_height = scene_bb[4] - scene_bb[1]
        # Create a new camera and fit it to the current view
        self.ui.build_progress.setValue(20)
        self.ui.status_label.setText('Creating camera...')
        logger.debug('Creating camera...')
        cam = cmds.camera(n='turn_table_cam')
        cmds.lookThru(cam)
        cmds.viewFit()
        self.ui.build_progress.setValue(21)
        self.ui.status_label.setText('Beginning camera position calculations...')
        logger.info('Beginning camera position calculations...')
        # Get the position of the new camera after placement
        cam_pos = cmds.xform(q=True, ws=True, t=True)
        logger.debug('Get initial camera position from frame.')
        # Separate out the mins and maxs of the bounding box for triangulation
        self.ui.build_progress.setValue(22)
        x_min = scene_bb[0]
        x_max = scene_bb[3]
        y_min = scene_bb[1]
        y_max = scene_bb[4]
        z_min = scene_bb[2]
        z_max = scene_bb[5]
        # Get the cube root hypotenuse of the bounding box to calculate the overall scene's widest distance
        self.ui.build_progress.setValue(24)
        logger.info('Calculating maximum scene scale...')
        cube_diff = math.pow((x_max - x_min), 3) + math.pow((y_max - y_min), 3) + math.pow((z_max - z_min), 3)
        max_hypotenuse = cube_diff ** (1. / 3.)
        # Cut the width in half to create a 90 degree angle
        self.ui.build_progress.setValue(26)
        res_width = float(self.ui.res_width.text())
        res_height = float(self.ui.res_height.text())
        aspect_ratio = res_width / res_height
        height = (y_max - y_min)
        width = (x_max - x_min)
        depth = (z_max - z_min)

        logger.debug('Set base frame width...')
        half_width = max_hypotenuse / 2
        # Get the horizontal aperture. Only the inch aperture is accessible, so mm aperture and field of view
        # must be calculated from that
        logger.debug('Get camera aperture and focal length...')
        horizontalApertureInch = cmds.getAttr('%s.horizontalFilmAperture' % cam[1])
        # convert to mm
        horizontalAperture_mm = 2.54 * horizontalApertureInch * 10
        # Get focal length
        focalLength = cmds.getAttr('%s.focalLength' % cam[1])
        # Calculate FOV from horizontal aperture and focal length
        self.ui.build_progress.setValue(27)
        logger.debug('Calculate the FOV...')
        fov = math.degrees(2 * math.atan(horizontalAperture_mm / (focalLength * 2)))
        # Cut the FOV in half to get angle of right angle.
        half_angle = fov / 2
        # Calculate the distance for the camera
        self.ui.build_progress.setValue(28)
        logger.info('Calculating the camera distance...')
        angle_tan = math.tan(half_angle)
        distance = cam_pos[2] - (half_width / angle_tan)
        # Set the new camera distance and height
        self.ui.build_progress.setValue(29)
        self.ui.status_label.setText('Adjusting camera position...')
        logger.debug('Repositioning camera...')
        cmds.setAttr('%s.ty' % cam[0], cam_height)
        cmds.setAttr('%s.tz' % cam[0], distance)
        # Get the new camera position
        new_cam_pos = cmds.xform(q=True, t=True, ws=True)
        # Calculate the decension angle from the center of the scene to the new camera position
        # TODO: Adjust this so that low cam angles look higher, and higher ones look lower.
        self.ui.build_progress.setValue(30)
        self.ui.status_label.setText('Adjusting camera angle...')
        logger.info('Calculating the camera angle...')
        # The camera height and distance are what is being used to create the angle calculation.
        # The Height calculation can be "inaccurate" on purpose to create a greater angle.
        # For instance, camera goes higher than 110% of the bounding box Y Max.
        # The height from the center point is no longer valid, the height should be increased to make the camera look
        # further down toward the base of the object at Y Min.
        # Or if the camera goes below center, the height should increase to look up at Y Max
        # print '-' * 100
        # print new_cam_pos[1]
        # print bb_center[1]
        # print 'ABSOLUTE DIFF: %s' % (new_cam_pos[1] - bb_center[1])

        cam_height = (new_cam_pos[1] - bb_center[1])
        logger.info('cam_height = %s' % cam_height)

        cam_dist = new_cam_pos[2] - bb_center[2]
        logger.info('cam_dist = %s' % cam_dist)
        # Turning this off until I figure out if I really need it.
        # if new_cam_pos[1] < bb_center[1]:
        #     limit = float(y_max) - bb_center[1]
        #     logger.info('limit = %s' % limit)
        #     overage = float(bb_center[1]) - new_cam_pos[1]
        #     logger.info('overage = %s' % overage)
        #     if overage > limit:
        #         overage = limit
        #     cam_height -= (overage/4)
        #     logger.info('cam_height = %s' % cam_height)
        cam_angle = -1 * (math.degrees(math.atan(cam_height / cam_dist)))
        logger.info('cam_angle = %s' % cam_angle)
        # Set the declination angle
        cmds.setAttr('%s.rx' % cam[0], cam_angle)
        # Group the camera, center the pivot, and animate the rotation

        self.ui.build_progress.setValue(32)
        self.ui.status_label.setText('Grouping the camera setup...')
        logger.debug('Grouping the camera setup...')
        cmds.group(n='_turntable_cam')
        cameras = cmds.listCameras(p=True, o=True)
        logger.debug('Set camera renderabilities for all cameras...')
        for camera in cameras:
            if camera == cam[0]:
                cmds.setAttr('%s.renderable' % camera, 1)
                cmds.setAttr('%s.translate' % camera, lock=True)
                cmds.setAttr('%s.rotate' % camera, lock=True)
                cmds.setAttr('%s.scale' % camera, lock=True)
            else:
                cmds.setAttr('%s.renderable' % camera, 0)
        logger.info('Camera setup complete!')
        return [cam, bb_center, scene_bb, max_hypotenuse]

    def animate_dome(self, trans=None, start=None, end=None):
        logger.info('Animating %s...' % trans)
        rot_range_type = self.ui.full_circle.isChecked()
        if rot_range_type:
            start_angle = 25.0
            end_angle = -335.0
        else:
            start_angle = float(self.ui.from_range.text())
            end_angle = float(self.ui.to_range.text())
        if trans:
            cmds.setKeyframe('%s.ry' % trans, v=start_angle, ott='linear', t=start)
            cmds.setKeyframe('%s.ry' % trans, v=end_angle, itt='linear', t=end)

    def create_draft_version(self, version_name=None, layer=None):
        version_title = '%s_%s' % (version_name, layer)
        data = {
            'project': {'type': 'Project', 'id': self.project_id},
            'description': 'Lazy Siouxsie Auto Turntable',
            'sg_status_list': 'rev',
            'code': version_title,
            'entity': {'type': 'Asset', 'id': self.entity_id},
            'sg_task': {'type': 'Task', 'id': self.tt_task}
        }
        version_data = self.sg.shotgun.create('Version', data)
        return version_data

    def submit_to_deadline(self, start=1, end=144, renderer=None, width=None, height=None, camera=None, layers=[]):
        logger.info('Submitting to Deadline...')
        self.ui.build_progress.setValue(77)
        self.ui.status_label.setText('Collect Deadline Pools...')
        logger.debug('Collecting the Deadline Pools...')
        all_pools = self.list_deadline_pools()
        ext = self.ui.render_format.currentText()

        self.ui.build_progress.setValue(78)
        self.ui.status_label.setText('Setup Deadline Environments and Datetime...')
        logger.debug('Setup Deadline Environment and Datetime...')
        file_name = cmds.file(q=True, sn=True)
        file_path = os.path.dirname(file_name)
        path_settings = self.sg.templates['maya_asset_work']
        task = path_settings.get_fields(file_name)
        base_name = os.path.basename(file_name).rsplit('.', 1)[0]
        project = self.project.lower()
        proj_root = '%s%s/assets/%s/%s' % (file_path.split(project)[0], project, task['sg_asset_type'], task['Asset'])
        # {'version': 67, 'sg_asset_type': u'Character', 'Asset': u'Thing3', 'task_name': u'turntable.main',
        #  'extension': u'mb'}
        output_path = '%s/publish/renders/' % proj_root
        version = task['version']
        t = 0
        logger.info('Parsing Render Layers into Render Jobs...')
        for layer in layers:
            lyr = str(layer)
            job_info = ''
            plugin_info = ''
            job_path = os.environ['TEMP'] + '\\_job_submissions'
            logger.debug('Checking job submission path...')
            if not os.path.exists(job_path):
                os.mkdir(job_path)
            logger.debug('Setting Job date and time...')
            h = datetime.now().hour
            m = datetime.now().minute
            s = datetime.now().second
            h = '%02d' % h
            m = '%02d' % m
            s = '%02d' % s
            D = datetime.now().day
            D = '%02d' % D
            M = datetime.now().month
            M = '%02d' % M
            Y = datetime.now().year
            d = '%s-%s-%s' % (D, M, Y)
            d_flat = str(d).replace('-', '')
            logger.debug('Creating job and plugin files...')
            ji_filename = '%s_%s%s%s%s%s_jobInfo.job' % (base_name, d_flat, h, m, s, t)
            ji_filepath = job_path + '\\' + ji_filename
            pi_filename = '%s_%s%s%s%s%s_pluginInfo.job' % (base_name, d_flat, h, m, s, t)
            pi_filepath = job_path + '\\' + pi_filename
            job_info_file = open(ji_filepath, 'w+')
            plugin_info_file = open(pi_filepath, 'w+')

            # Create a Shotgun Version for Draft...
            logger.info('Creating Shotgun Version for layer %s...' % lyr)
            draft = self.create_draft_version(version_name=base_name, layer=lyr)

            # Setup JobInfo
            logger.debug('Collecting user, resolution, frames and pool data...')
            user_name = os.environ['USERNAME']
            frames = '%s-%s' % (start, end)
            pool = None
            for p in all_pools:
                if renderer in p:
                    pool = p
                    break

            version_name = '%s_%s' % (base_name, lyr)

            resolutionWidth = int(self.ui.res_width.text())
            resolutionHeight = int(self.ui.res_height.text())
            resolution_scale = self.ui.res_scale.currentText()
            resolution_scale = float(resolution_scale.strip('%'))
            resolution_scale /= 100
            resolutionHeight *= resolution_scale
            resolutionWidth *= resolution_scale

            self.ui.build_progress.setValue(79)
            self.ui.status_label.setText('Create Job Info File...')
            logger.debug('Creating Job Info File...')
            job_info += 'Name=%s - %s\n' % (base_name, lyr)
            job_info += 'BatchName=%s\n' % base_name
            job_info += 'UserName=%s\n' % user_name
            job_info += 'Region=none\n'
            job_info += 'Comment=Lazy Siouxsie Automatic Turntable\n'
            job_info += 'Frames=%s\n' % frames
            job_info += 'Pool=%s\n' % pool
            job_info += 'Priority=65\n'
            job_info += 'Blacklist=\n'
            job_info += 'MachineLimit=5\n'
            job_info += 'ScheduledStartDateTime=%s/%s/%s %s:%s\n' % (D, M, Y, h, m)
            job_info += 'ExtraInfo0=%s\n' % task['task_name']
            job_info += 'ExtraInfo1=%s\n' % project
            job_info += 'ExtraInfo2=%s\n' % task['Asset']
            job_info += 'ExtraInfo3=%s\n' % version_name
            job_info += 'ExtraInfo4=Lazy Siouxsie Auto Turntable\n'
            job_info += 'ExtraInfo5=%s\n' % user_name
            # Draft Submission details
            # TODO: Rework the Draft Submission
            # The following needs to be added after the main submission.
            # Essentially, Submit the job, find the version ID that it created, and then amend the Job Properties with
            # the following.  For now, it will just create 2 different versions that don't entirely work right.
            # small price to pay for the moment.
            job_info += 'ExtraInfoKeyValue0=UserName=%s\n' % user_name
            job_info += 'ExtraInfoKeyValue1=DraftFrameRate=24\n'
            job_info += 'ExtraInfoKeyValue2=DraftExtension=mov\n'
            job_info += 'ExtraInfoKeyValue3=DraftCodec=h264\n'
            job_info += 'ExtraInfoKeyValue4=DraftQuality=100\n'
            job_info += 'ExtraInfoKeyValue5=Description=Lazy Siouxsie Turntable Draft\n'
            job_info += 'ExtraInfoKeyValue6=ProjectName=%s\n' % project
            job_info += 'ExtraInfoKeyValue7=EntityName=%s\n' % task['Asset']
            job_info += 'ExtraInfoKeyValue8=EntityType=Asset\n'
            job_info += 'ExtraInfoKeyValue9=DraftType=movie\n'
            job_info += 'ExtraInfoKeyValue10=VersionId=%s\n' % draft['id']
            job_info += 'ExtraInfoKeyValue11=DraftColorSpaceIn=Identity\n'
            job_info += 'ExtraInfoKeyValue12=DraftColorSpaceOut=Identity\n'
            job_info += 'ExtraInfoKeyValue13=VersionName=%s\n' % version_name
            job_info += 'ExtraInfoKeyValue14=TaskId=-1\n'
            job_info += 'ExtraInfoKeyValue15=ProjectId=%s\n' % self.project_id
            job_info += 'ExtraInfoKeyValue16=DraftUploadToShotgun=True\n'
            job_info += 'ExtraInfoKeyValue17=TaskName=%s\n' % task['task_name']
            job_info += 'ExtraInfoKeyValue18=DraftResolution=1\n'
            job_info += 'ExtraInfoKeyValue19=EntityId=%s\n' % self.entity_id
            job_info += 'ExtraInfoKeyValue20=SubmitQuickDraft=True\n'
            # End Draft Submission details
            job_info += 'OverrideTaskExtraInfoNames=False\n'
            job_info += 'MachineName=%s\n' % platform.node()
            job_info += 'Plugin=MayaCmd\n'
            output_file = '%s_%s.####.%s' % (layer, base_name, ext)
            output_directory = '%s%s/%s/v%03d' % (output_path, task['task_name'], layer, version)
            # output_directory = output_directory.replace('/', '\\')
            job_info += 'OutputDirectory0=%s\n' % output_directory
            job_info += 'OutputFilename0=%s\n' % output_file
            job_info += 'EventOptIns='
            job_info_file.write(job_info)
            job_info_file.close()

            # Setup PluginInfo
            self.ui.build_progress.setValue(80)
            self.ui.status_label.setText('Build Plugin Info File...')
            logger.debug('Creating PluginInfo file...')
            plugin_info += 'Animation=1\n'
            plugin_info += 'Renderer=%s\n' % renderer
            plugin_info += 'UsingRenderLayers=1\n'
            plugin_info += 'RenderLayer=\n'
            plugin_info += 'RenderHalfFrames=0\n'
            plugin_info += 'FrameNumberOffset=0\n'
            plugin_info += 'LocalRendering=0\n'
            plugin_info += 'StrictErrorChecking=0\n'
            plugin_info += 'MaxProcessors=0\n'
            plugin_info += 'Version=%s\n' % cmds.about(q=True, v=True)
            plugin_info += 'UsingLegacyRenderLayers=0\n'
            if cmds.about(q=True, w64=True):
                win = '64bit'
            else:
                win = '32bit'
            plugin_info += 'Build=%s\n' % win
            plugin_info += 'ProjectPath=%s\n' % proj_root
            plugin_info += 'CommandLineOptions=\n'
            plugin_info += 'ImageWidth=%s\n' % resolutionWidth
            plugin_info += 'ImageHeight=%s\n' % resolutionHeight
            plugin_info += 'OutputFilePath=%s\n' % output_path
            plugin_info += 'OutputFilePrefix=\n'
            plugin_info += 'Camera=%s\n' % camera[0]
            plugin_info += 'Camera0=\nCamera1=%s\n' % camera[0]
            plugin_info += 'Camera2=front\nCamera3=persp\nCamera4=side\nCamera5=top\n'
            plugin_info += 'SceneFile=%s\n' % file_name
            plugin_info += 'IgnoreError211=1\n'
            plugin_info += 'UseOnlyCommandLineOptions=False\n'
            plugin_info_file.write(plugin_info)
            plugin_info_file.close()

            self.ui.build_progress.setValue(81)
            self.ui.status_label.setText('Getting slice status. Ignore 0 degrees...')
            logger.debug('Getting slice status.  Ignoring 0 degrees...')
            degree_slice = self.ui.render_slices.currentText()
            degree = float(degree_slice)
            frame_range = float(end - start + 1)
            slice_mult = (frame_range/2) / 360.00
            slice_frames = int(slice_mult * degree)
            slice_frame = 0
            try:
                self.ui.build_progress.setValue(82)
                self.ui.status_label.setText('Submitting the Job to Deadline...')
                logger.info('Submitting the job to Deadline...')
                submitted = self.dl.Jobs.SubmitJobFiles(ji_filepath, pi_filepath, idOnly=True)
                # TODO: The following example is the basic idea behind submitting the python file:
                # submitted = self.dl.Jobs.SubmitJobFiles(ji_filepath, pi_filepath, aux=[pythonFile], idOnly=True)
                # How that's fully implemented remains to be figured out.

                # Setup slice conditions here, to then suspend specific job tasks.
                if submitted and degree != 0:
                    self.ui.build_progress.setValue(83)
                    self.ui.status_label.setText('Parsing Slices...')
                    logger.info('Parsing slices....')
                    job_id = submitted['_id']
                    tasks = self.dl.Tasks.GetJobTasks(job_id)
                    task_count = len(tasks)
                    task_percent = 12.0 / float(task_count)
                    percent = 84.0
                    task_list = []
                    for tsk in tasks['Tasks']:
                        task_id = int(tsk['TaskID'])
                        percent += task_percent
                        if task_id != slice_frame:
                            task_list.append(task_id)
                        else:
                            self.ui.build_progress.setValue(int(percent))
                            self.ui.status_label.setText('Setting %i Frame to Render...' % task_id)
                            logger.debug('Rendering frame %s' % task_id)
                            slice_frame += slice_frames
                    if task_list:
                        logger.debug('Suspending non-sliced tasks...')
                        self.dl.Tasks.SuspendJobTasks(jobId=job_id, taskIds=task_list)
            except Exception as e:
                submitted = False
                logger.error('JOB SUBMISSION FAILED! %s' % e)
            t += 1

    def list_deadline_pools(self):
        try:
            # pools = ['none', 'maya_vray', 'nuke', 'maya_redshift', 'houdini', 'alembics', 'arnold', 'caching']
            logger.debug('Return Deadline pools.')
            pools = self.dl.Pools.GetPoolNames()
        except Exception:
            pools = []
        return pools

    def do_preflight_check(self):
        system_parts = [
            '_Turntable_Set_Prep',
            '_turntable_cam',
            'turn_table_cam1',
            '_HDRI_light',
            '_turntable_ground_plane',
            '_turntable_chrome_ball',
            '_turntable_gray_ball'
        ]
        for part in system_parts:
            if cmds.objExists(part):
                self.ui.status_label.setText('Turntable parts are already found in the scene! Run from a clean scene.')
                logger.warning('This scene has previous turntable configuration parts in it.  Open a clean file!')
                return False
        file_name = cmds.file(q=True, sn=True)
        if self.turntable_task in file_name:
            self.ui.status_label.setText('It looks like this is already a turntable file. Run from a clean scene.')
            logger.warning('This is already a turntable file, and the setup should already be done.  Try running the '
                           'tool from a model or lookdev file.')
            return False
        all_geo = cmds.ls(type=['mesh', 'nurbsSurface'])
        grounds = []
        for geo in all_geo:
            if 'ground' in geo.lower():
                grounds.append(geo)
        if grounds:
            self.ui.ground_plane.setChecked(False)
            logger.debug('Ground plane detected.  Turning off auto ground plane.')
            self.ground_plane = grounds
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    window = LazySiouxsie()
    window.show()
    app.exec_(sys.argv)
