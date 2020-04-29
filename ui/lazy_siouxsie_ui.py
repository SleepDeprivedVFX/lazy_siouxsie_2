# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lazy_siouxsie_uiixiIuA.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_lazySiouxsie(object):
    def setupUi(self, lazySiouxsie):
        if lazySiouxsie.objectName():
            lazySiouxsie.setObjectName(u"lazySiouxsie")
        lazySiouxsie.resize(557, 804)
        lazySiouxsie.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(240, 240, 240);")
        self.verticalLayout_2 = QVBoxLayout(lazySiouxsie)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(lazySiouxsie)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"font: 75 italic 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.title)

        self.subTitle = QLabel(lazySiouxsie)
        self.subTitle.setObjectName(u"subTitle")
        self.subTitle.setStyleSheet(u"font: 75 italic 10pt \"MS Shell Dlg 2\";")
        self.subTitle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.subTitle)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.file_label = QLabel(lazySiouxsie)
        self.file_label.setObjectName(u"file_label")

        self.horizontalLayout_5.addWidget(self.file_label)

        self.file_path = QLineEdit(lazySiouxsie)
        self.file_path.setObjectName(u"file_path")

        self.horizontalLayout_5.addWidget(self.file_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hdri_label = QLabel(lazySiouxsie)
        self.hdri_label.setObjectName(u"hdri_label")
        self.hdri_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.hdri_label)

        self.hdriList = QListWidget(lazySiouxsie)
        self.hdriList.setObjectName(u"hdriList")
        self.hdriList.setAlternatingRowColors(True)
        self.hdriList.setSelectionMode(QAbstractItemView.MultiSelection)

        self.horizontalLayout.addWidget(self.hdriList)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.custom = QLabel(lazySiouxsie)
        self.custom.setObjectName(u"custom")

        self.horizontalLayout_3.addWidget(self.custom)

        self.custom_hdri = QLineEdit(lazySiouxsie)
        self.custom_hdri.setObjectName(u"custom_hdri")

        self.horizontalLayout_3.addWidget(self.custom_hdri)

        self.browse_btn = QPushButton(lazySiouxsie)
        self.browse_btn.setObjectName(u"browse_btn")

        self.horizontalLayout_3.addWidget(self.browse_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frame_statement = QLabel(lazySiouxsie)
        self.frame_statement.setObjectName(u"frame_statement")
        self.frame_statement.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.frame_statement)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startLabel = QLabel(lazySiouxsie)
        self.startLabel.setObjectName(u"startLabel")

        self.horizontalLayout_2.addWidget(self.startLabel)

        self.startFrame = QSpinBox(lazySiouxsie)
        self.startFrame.setObjectName(u"startFrame")
        self.startFrame.setMaximum(50000)
        self.startFrame.setValue(1001)

        self.horizontalLayout_2.addWidget(self.startFrame)

        self.endLabel = QLabel(lazySiouxsie)
        self.endLabel.setObjectName(u"endLabel")

        self.horizontalLayout_2.addWidget(self.endLabel)

        self.endFrame = QSpinBox(lazySiouxsie)
        self.endFrame.setObjectName(u"endFrame")
        self.endFrame.setMaximum(50000)
        self.endFrame.setValue(1072)

        self.horizontalLayout_2.addWidget(self.endFrame)

        self.totalFrameLabel = QLabel(lazySiouxsie)
        self.totalFrameLabel.setObjectName(u"totalFrameLabel")

        self.horizontalLayout_2.addWidget(self.totalFrameLabel)

        self.total_frames = QLineEdit(lazySiouxsie)
        self.total_frames.setObjectName(u"total_frames")
        self.total_frames.setMaximumSize(QSize(75, 16777215))
        self.total_frames.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.total_frames)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.rot_range_label = QLabel(lazySiouxsie)
        self.rot_range_label.setObjectName(u"rot_range_label")

        self.horizontalLayout_12.addWidget(self.rot_range_label)

        self.full_circle = QRadioButton(lazySiouxsie)
        self.full_circle.setObjectName(u"full_circle")
        self.full_circle.setLayoutDirection(Qt.RightToLeft)
        self.full_circle.setChecked(True)

        self.horizontalLayout_12.addWidget(self.full_circle)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.partial_circle = QRadioButton(lazySiouxsie)
        self.partial_circle.setObjectName(u"partial_circle")
        self.partial_circle.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_12.addWidget(self.partial_circle)

        self.from_label = QLabel(lazySiouxsie)
        self.from_label.setObjectName(u"from_label")

        self.horizontalLayout_12.addWidget(self.from_label)

        self.from_range = QLineEdit(lazySiouxsie)
        self.from_range.setObjectName(u"from_range")
        self.from_range.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_12.addWidget(self.from_range)

        self.to_label = QLabel(lazySiouxsie)
        self.to_label.setObjectName(u"to_label")

        self.horizontalLayout_12.addWidget(self.to_label)

        self.to_range = QLineEdit(lazySiouxsie)
        self.to_range.setObjectName(u"to_range")
        self.to_range.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_12.addWidget(self.to_range)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.resolution_label = QLabel(lazySiouxsie)
        self.resolution_label.setObjectName(u"resolution_label")

        self.horizontalLayout_6.addWidget(self.resolution_label)

        self.res_width = QLineEdit(lazySiouxsie)
        self.res_width.setObjectName(u"res_width")
        self.res_width.setMaximumSize(QSize(120, 16777215))
        self.res_width.setMaxLength(8)

        self.horizontalLayout_6.addWidget(self.res_width)

        self.x_label = QLabel(lazySiouxsie)
        self.x_label.setObjectName(u"x_label")

        self.horizontalLayout_6.addWidget(self.x_label)

        self.res_height = QLineEdit(lazySiouxsie)
        self.res_height.setObjectName(u"res_height")
        self.res_height.setMaximumSize(QSize(120, 16777215))
        self.res_height.setMaxLength(8)

        self.horizontalLayout_6.addWidget(self.res_height)

        self.res_scale = QComboBox(lazySiouxsie)
        self.res_scale.addItem("")
        self.res_scale.addItem("")
        self.res_scale.addItem("")
        self.res_scale.addItem("")
        self.res_scale.addItem("")
        self.res_scale.addItem("")
        self.res_scale.setObjectName(u"res_scale")

        self.horizontalLayout_6.addWidget(self.res_scale)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pixel_aspect_label = QLabel(lazySiouxsie)
        self.pixel_aspect_label.setObjectName(u"pixel_aspect_label")

        self.horizontalLayout_8.addWidget(self.pixel_aspect_label)

        self.pixel_aspect = QLineEdit(lazySiouxsie)
        self.pixel_aspect.setObjectName(u"pixel_aspect")
        self.pixel_aspect.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.pixel_aspect)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.camera_height_label = QLabel(lazySiouxsie)
        self.camera_height_label.setObjectName(u"camera_height_label")

        self.horizontalLayout_8.addWidget(self.camera_height_label)

        self.camera_height = QLineEdit(lazySiouxsie)
        self.camera_height.setObjectName(u"camera_height")
        self.camera_height.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.camera_height)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.render_engine_label = QLabel(lazySiouxsie)
        self.render_engine_label.setObjectName(u"render_engine_label")

        self.horizontalLayout_7.addWidget(self.render_engine_label)

        self.rendering_engine = QComboBox(lazySiouxsie)
        self.rendering_engine.addItem("")
        self.rendering_engine.addItem("")
        self.rendering_engine.addItem("")
        self.rendering_engine.addItem("")
        self.rendering_engine.addItem("")
        self.rendering_engine.setObjectName(u"rendering_engine")

        self.horizontalLayout_7.addWidget(self.rendering_engine)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.render_slices_label = QLabel(lazySiouxsie)
        self.render_slices_label.setObjectName(u"render_slices_label")

        self.horizontalLayout_7.addWidget(self.render_slices_label)

        self.render_slices = QComboBox(lazySiouxsie)
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.addItem("")
        self.render_slices.setObjectName(u"render_slices")
        self.render_slices.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_7.addWidget(self.render_slices)

        self.degreeLabel = QLabel(lazySiouxsie)
        self.degreeLabel.setObjectName(u"degreeLabel")

        self.horizontalLayout_7.addWidget(self.degreeLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(lazySiouxsie)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.render_format = QComboBox(lazySiouxsie)
        self.render_format.addItem("")
        self.render_format.addItem("")
        self.render_format.addItem("")
        self.render_format.setObjectName(u"render_format")

        self.horizontalLayout_11.addWidget(self.render_format)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.quality_label = QLabel(lazySiouxsie)
        self.quality_label.setObjectName(u"quality_label")

        self.horizontalLayout_10.addWidget(self.quality_label)

        self.quality_slider = QSlider(lazySiouxsie)
        self.quality_slider.setObjectName(u"quality_slider")
        self.quality_slider.setMinimum(1)
        self.quality_slider.setMaximum(10)
        self.quality_slider.setValue(7)
        self.quality_slider.setOrientation(Qt.Horizontal)
        self.quality_slider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_10.addWidget(self.quality_slider)

        self.quality_value = QSpinBox(lazySiouxsie)
        self.quality_value.setObjectName(u"quality_value")
        self.quality_value.setMinimum(1)
        self.quality_value.setMaximum(10)
        self.quality_value.setValue(7)

        self.horizontalLayout_10.addWidget(self.quality_value)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.scene_lights = QCheckBox(lazySiouxsie)
        self.scene_lights.setObjectName(u"scene_lights")
        self.scene_lights.setEnabled(True)
        self.scene_lights.setLayoutDirection(Qt.RightToLeft)
        self.scene_lights.setChecked(True)

        self.horizontalLayout_9.addWidget(self.scene_lights)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.ground_plane = QCheckBox(lazySiouxsie)
        self.ground_plane.setObjectName(u"ground_plane")
        self.ground_plane.setLayoutDirection(Qt.RightToLeft)
        self.ground_plane.setChecked(True)

        self.horizontalLayout_9.addWidget(self.ground_plane)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.chrome_balls = QCheckBox(lazySiouxsie)
        self.chrome_balls.setObjectName(u"chrome_balls")
        self.chrome_balls.setLayoutDirection(Qt.RightToLeft)
        self.chrome_balls.setChecked(True)

        self.horizontalLayout_9.addWidget(self.chrome_balls)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.open_turntable = QCheckBox(lazySiouxsie)
        self.open_turntable.setObjectName(u"open_turntable")

        self.horizontalLayout_13.addWidget(self.open_turntable)

        self.submit_to_deadline = QCheckBox(lazySiouxsie)
        self.submit_to_deadline.setObjectName(u"submit_to_deadline")
        self.submit_to_deadline.setLayoutDirection(Qt.RightToLeft)
        self.submit_to_deadline.setChecked(True)

        self.horizontalLayout_13.addWidget(self.submit_to_deadline)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.build_progress = QProgressBar(lazySiouxsie)
        self.build_progress.setObjectName(u"build_progress")
        self.build_progress.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"	color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(224, 149, 0);\n"
"    width: 20px;\n"
"	margin: 1px;\n"
"}")
        self.build_progress.setValue(24)

        self.verticalLayout.addWidget(self.build_progress)

        self.status_label = QLabel(lazySiouxsie)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout.addWidget(self.status_label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(lazySiouxsie)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_4.addWidget(self.cancel_btn)

        self.spin_btn = QPushButton(lazySiouxsie)
        self.spin_btn.setObjectName(u"spin_btn")

        self.horizontalLayout_4.addWidget(self.spin_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

#if QT_CONFIG(shortcut)
        self.file_label.setBuddy(self.file_path)
        self.hdri_label.setBuddy(self.hdriList)
        self.custom.setBuddy(self.custom_hdri)
        self.startLabel.setBuddy(self.startFrame)
        self.endLabel.setBuddy(self.endFrame)
        self.totalFrameLabel.setBuddy(self.total_frames)
        self.from_label.setBuddy(self.from_range)
        self.to_label.setBuddy(self.to_range)
        self.resolution_label.setBuddy(self.res_width)
        self.pixel_aspect_label.setBuddy(self.pixel_aspect)
        self.camera_height_label.setBuddy(self.camera_height)
        self.render_engine_label.setBuddy(self.rendering_engine)
        self.render_slices_label.setBuddy(self.render_slices)
        self.quality_label.setBuddy(self.quality_slider)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.spin_btn, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.browse_btn)
        QWidget.setTabOrder(self.browse_btn, self.startFrame)
        QWidget.setTabOrder(self.startFrame, self.endFrame)
        QWidget.setTabOrder(self.endFrame, self.res_scale)
        QWidget.setTabOrder(self.res_scale, self.camera_height)
        QWidget.setTabOrder(self.camera_height, self.rendering_engine)
        QWidget.setTabOrder(self.rendering_engine, self.render_slices)
        QWidget.setTabOrder(self.render_slices, self.render_format)
        QWidget.setTabOrder(self.render_format, self.quality_value)
        QWidget.setTabOrder(self.quality_value, self.scene_lights)
        QWidget.setTabOrder(self.scene_lights, self.ground_plane)
        QWidget.setTabOrder(self.ground_plane, self.chrome_balls)
        QWidget.setTabOrder(self.chrome_balls, self.submit_to_deadline)
        QWidget.setTabOrder(self.submit_to_deadline, self.full_circle)
        QWidget.setTabOrder(self.full_circle, self.partial_circle)
        QWidget.setTabOrder(self.partial_circle, self.from_range)
        QWidget.setTabOrder(self.from_range, self.to_range)
        QWidget.setTabOrder(self.to_range, self.res_width)
        QWidget.setTabOrder(self.res_width, self.res_height)
        QWidget.setTabOrder(self.res_height, self.pixel_aspect)
        QWidget.setTabOrder(self.pixel_aspect, self.quality_slider)
        QWidget.setTabOrder(self.quality_slider, self.hdriList)
        QWidget.setTabOrder(self.hdriList, self.custom_hdri)
        QWidget.setTabOrder(self.custom_hdri, self.total_frames)
        QWidget.setTabOrder(self.total_frames, self.file_path)

        self.retranslateUi(lazySiouxsie)
        self.quality_slider.valueChanged.connect(self.quality_value.setValue)
        self.quality_value.valueChanged.connect(self.quality_slider.setValue)

        self.hdriList.setCurrentRow(-1)
        self.res_scale.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(lazySiouxsie)
    # setupUi

    def retranslateUi(self, lazySiouxsie):
        lazySiouxsie.setWindowTitle(QCoreApplication.translate("lazySiouxsie", u"Lazy Siouzsie", None))
        self.title.setText(QCoreApplication.translate("lazySiouxsie", u"Lazy Siouxsie", None))
        self.subTitle.setText(QCoreApplication.translate("lazySiouxsie", u"Auto Turntable Machine", None))
#if QT_CONFIG(tooltip)
        self.file_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The current file being Turn Tabled", None))
#endif // QT_CONFIG(tooltip)
        self.file_label.setText(QCoreApplication.translate("lazySiouxsie", u"File", None))
#if QT_CONFIG(tooltip)
        self.file_path.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The current file being Turn Tabled", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.file_path.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The current file being Turn Tabled", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.file_path.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The current file being Turn Tabled", None))
#endif // QT_CONFIG(whatsthis)
        self.file_path.setPlaceholderText(QCoreApplication.translate("lazySiouxsie", u"The Current File to be sent to the farm", None))
#if QT_CONFIG(tooltip)
        self.hdri_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"HDRII list provided by a Shotgun directory of Studio HDRIs", None))
#endif // QT_CONFIG(tooltip)
        self.hdri_label.setText(QCoreApplication.translate("lazySiouxsie", u"HDRIs", None))
#if QT_CONFIG(tooltip)
        self.hdriList.setToolTip(QCoreApplication.translate("lazySiouxsie", u"HDRI list provided by a Shotgun directory of Studio HDRIs", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.hdriList.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"HDRI list provided by a Shotgun directory of Studio HDRIs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.hdriList.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"HDRI list provided by a Shotgun directory of Studio HDRIs", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.custom.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(tooltip)
        self.custom.setText(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI", None))
#if QT_CONFIG(tooltip)
        self.custom_hdri.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.custom_hdri.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.custom_hdri.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(whatsthis)
        self.custom_hdri.setPlaceholderText(QCoreApplication.translate("lazySiouxsie", u"If a show/shot specific HDRI is needed", None))
#if QT_CONFIG(tooltip)
        self.browse_btn.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.browse_btn.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.browse_btn.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Custom HDRI file, if a specific file is desired", None))
#endif // QT_CONFIG(whatsthis)
        self.browse_btn.setText(QCoreApplication.translate("lazySiouxsie", u"Browse", None))
        self.frame_statement.setText(QCoreApplication.translate("lazySiouxsie", u"The Start and End times are for the initial rotation.  A second rotation of equal time will be added to spin the HDRI around the object.  The Total Frames represents first and second rotations for each HDRI", None))
#if QT_CONFIG(tooltip)
        self.startLabel.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Starting frame of Camera animation.", None))
#endif // QT_CONFIG(tooltip)
        self.startLabel.setText(QCoreApplication.translate("lazySiouxsie", u"Start Frame", None))
#if QT_CONFIG(tooltip)
        self.startFrame.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Starting frame of Camera animation.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.startFrame.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Starting frame of Camera animation.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.startFrame.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Starting frame of Camera animation.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.endLabel.setToolTip(QCoreApplication.translate("lazySiouxsie", u"End frame of the Camera Animation.  HDRI Spin will be added to this time", None))
#endif // QT_CONFIG(tooltip)
        self.endLabel.setText(QCoreApplication.translate("lazySiouxsie", u"End Frame", None))
#if QT_CONFIG(tooltip)
        self.endFrame.setToolTip(QCoreApplication.translate("lazySiouxsie", u"End frame of the Camera Animation.  HDRI Spin will be added to this time", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.endFrame.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"End frame of the Camera Animation.  HDRI Spin will be added to this time", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.endFrame.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"End frame of the Camera Animation.  HDRI Spin will be added to this time", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.totalFrameLabel.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Total frames of animation is the Camera Rotation plus an HDRI rotation of the same value.  Thus, double the frames", None))
#endif // QT_CONFIG(tooltip)
        self.totalFrameLabel.setText(QCoreApplication.translate("lazySiouxsie", u"Total Frames:", None))
#if QT_CONFIG(tooltip)
        self.total_frames.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Total frames of animation is the Camera Rotation plus an HDRI rotation of the same value.  Thus, double the frames", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.total_frames.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Total frames of animation is the Camera Rotation plus an HDRI rotation of the same value.  Thus, double the frames", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.total_frames.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Total frames of animation is the Camera Rotation plus an HDRI rotation of the same value.  Thus, double the frames", None))
#endif // QT_CONFIG(whatsthis)
        self.total_frames.setText(QCoreApplication.translate("lazySiouxsie", u"144", None))
        self.rot_range_label.setText(QCoreApplication.translate("lazySiouxsie", u"Rotation Range:", None))
        self.full_circle.setText(QCoreApplication.translate("lazySiouxsie", u"360\u00b0", None))
        self.partial_circle.setText(QCoreApplication.translate("lazySiouxsie", u"Range", None))
        self.from_label.setText(QCoreApplication.translate("lazySiouxsie", u"From:", None))
        self.from_range.setText(QCoreApplication.translate("lazySiouxsie", u"90", None))
        self.to_label.setText(QCoreApplication.translate("lazySiouxsie", u"To:", None))
        self.to_range.setText(QCoreApplication.translate("lazySiouxsie", u"-90", None))
#if QT_CONFIG(tooltip)
        self.resolution_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.resolution_label.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.resolution_label.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(whatsthis)
        self.resolution_label.setText(QCoreApplication.translate("lazySiouxsie", u"Resolution", None))
#if QT_CONFIG(tooltip)
        self.res_width.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.res_width.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.res_width.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(whatsthis)
        self.x_label.setText(QCoreApplication.translate("lazySiouxsie", u"X", None))
#if QT_CONFIG(tooltip)
        self.res_height.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.res_height.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.res_height.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Resolution set by Shotgun if available", None))
#endif // QT_CONFIG(whatsthis)
        self.res_scale.setItemText(0, QCoreApplication.translate("lazySiouxsie", u"25%", None))
        self.res_scale.setItemText(1, QCoreApplication.translate("lazySiouxsie", u"50%", None))
        self.res_scale.setItemText(2, QCoreApplication.translate("lazySiouxsie", u"75%", None))
        self.res_scale.setItemText(3, QCoreApplication.translate("lazySiouxsie", u"100%", None))
        self.res_scale.setItemText(4, QCoreApplication.translate("lazySiouxsie", u"150%", None))
        self.res_scale.setItemText(5, QCoreApplication.translate("lazySiouxsie", u"200%", None))

#if QT_CONFIG(tooltip)
        self.res_scale.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Resolution scale will change the final render size.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.res_scale.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Resolution scale will change the final render size.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.res_scale.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Resolution scale will change the final render size.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.pixel_aspect_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Pixel aspect set by Shotgun if it's available", None))
#endif // QT_CONFIG(tooltip)
        self.pixel_aspect_label.setText(QCoreApplication.translate("lazySiouxsie", u"Pixel Aspect", None))
#if QT_CONFIG(tooltip)
        self.pixel_aspect.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Pixel aspect set by Shotgun if it's available", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pixel_aspect.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Pixel aspect set by Shotgun if it's available", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pixel_aspect.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Pixel aspect set by Shotgun if it's available", None))
#endif // QT_CONFIG(whatsthis)
        self.pixel_aspect.setText(QCoreApplication.translate("lazySiouxsie", u"1.0", None))
#if QT_CONFIG(tooltip)
        self.camera_height_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.camera_height_label.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.camera_height_label.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(whatsthis)
        self.camera_height_label.setText(QCoreApplication.translate("lazySiouxsie", u"Camera Height", None))
#if QT_CONFIG(tooltip)
        self.camera_height.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.camera_height.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.camera_height.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Height off the ground in Maya Units.  If left blank, camara uses the default calculation", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.render_engine_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.render_engine_label.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.render_engine_label.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(whatsthis)
        self.render_engine_label.setText(QCoreApplication.translate("lazySiouxsie", u"Rendering Engine", None))
        self.rendering_engine.setItemText(0, QCoreApplication.translate("lazySiouxsie", u"arnold", None))
        self.rendering_engine.setItemText(1, QCoreApplication.translate("lazySiouxsie", u"vray", None))
        self.rendering_engine.setItemText(2, QCoreApplication.translate("lazySiouxsie", u"redshift", None))
        self.rendering_engine.setItemText(3, QCoreApplication.translate("lazySiouxsie", u"renderman", None))
        self.rendering_engine.setItemText(4, QCoreApplication.translate("lazySiouxsie", u"mayasoftware", None))

#if QT_CONFIG(tooltip)
        self.rendering_engine.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.rendering_engine.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.rendering_engine.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The Rendering Engine.  Selected by Shotgun if it is available.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.render_slices_label.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.render_slices_label.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.render_slices_label.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(whatsthis)
        self.render_slices_label.setText(QCoreApplication.translate("lazySiouxsie", u"Render Slices", None))
        self.render_slices.setItemText(0, QCoreApplication.translate("lazySiouxsie", u"0", None))
        self.render_slices.setItemText(1, QCoreApplication.translate("lazySiouxsie", u"5", None))
        self.render_slices.setItemText(2, QCoreApplication.translate("lazySiouxsie", u"10", None))
        self.render_slices.setItemText(3, QCoreApplication.translate("lazySiouxsie", u"15", None))
        self.render_slices.setItemText(4, QCoreApplication.translate("lazySiouxsie", u"20", None))
        self.render_slices.setItemText(5, QCoreApplication.translate("lazySiouxsie", u"25", None))
        self.render_slices.setItemText(6, QCoreApplication.translate("lazySiouxsie", u"30", None))
        self.render_slices.setItemText(7, QCoreApplication.translate("lazySiouxsie", u"35", None))
        self.render_slices.setItemText(8, QCoreApplication.translate("lazySiouxsie", u"40", None))
        self.render_slices.setItemText(9, QCoreApplication.translate("lazySiouxsie", u"45", None))
        self.render_slices.setItemText(10, QCoreApplication.translate("lazySiouxsie", u"50", None))
        self.render_slices.setItemText(11, QCoreApplication.translate("lazySiouxsie", u"55", None))
        self.render_slices.setItemText(12, QCoreApplication.translate("lazySiouxsie", u"60", None))
        self.render_slices.setItemText(13, QCoreApplication.translate("lazySiouxsie", u"65", None))
        self.render_slices.setItemText(14, QCoreApplication.translate("lazySiouxsie", u"70", None))
        self.render_slices.setItemText(15, QCoreApplication.translate("lazySiouxsie", u"75", None))
        self.render_slices.setItemText(16, QCoreApplication.translate("lazySiouxsie", u"80", None))
        self.render_slices.setItemText(17, QCoreApplication.translate("lazySiouxsie", u"85", None))
        self.render_slices.setItemText(18, QCoreApplication.translate("lazySiouxsie", u"90", None))
        self.render_slices.setItemText(19, QCoreApplication.translate("lazySiouxsie", u"95", None))
        self.render_slices.setItemText(20, QCoreApplication.translate("lazySiouxsie", u"100", None))
        self.render_slices.setItemText(21, QCoreApplication.translate("lazySiouxsie", u"105", None))
        self.render_slices.setItemText(22, QCoreApplication.translate("lazySiouxsie", u"110", None))
        self.render_slices.setItemText(23, QCoreApplication.translate("lazySiouxsie", u"115", None))
        self.render_slices.setItemText(24, QCoreApplication.translate("lazySiouxsie", u"120", None))
        self.render_slices.setItemText(25, QCoreApplication.translate("lazySiouxsie", u"125", None))
        self.render_slices.setItemText(26, QCoreApplication.translate("lazySiouxsie", u"130", None))
        self.render_slices.setItemText(27, QCoreApplication.translate("lazySiouxsie", u"135", None))
        self.render_slices.setItemText(28, QCoreApplication.translate("lazySiouxsie", u"140", None))
        self.render_slices.setItemText(29, QCoreApplication.translate("lazySiouxsie", u"145", None))
        self.render_slices.setItemText(30, QCoreApplication.translate("lazySiouxsie", u"150", None))
        self.render_slices.setItemText(31, QCoreApplication.translate("lazySiouxsie", u"155", None))
        self.render_slices.setItemText(32, QCoreApplication.translate("lazySiouxsie", u"160", None))
        self.render_slices.setItemText(33, QCoreApplication.translate("lazySiouxsie", u"165", None))
        self.render_slices.setItemText(34, QCoreApplication.translate("lazySiouxsie", u"170", None))
        self.render_slices.setItemText(35, QCoreApplication.translate("lazySiouxsie", u"175", None))
        self.render_slices.setItemText(36, QCoreApplication.translate("lazySiouxsie", u"180", None))

#if QT_CONFIG(tooltip)
        self.render_slices.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.render_slices.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.render_slices.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The render slices set a percentage of frames to be rendered based on rotational degrees. All frames will be submitted to the farm, but only frames at the chosen angle will automatically be rendered, leaving the remaining frames suspended. 0\u00b0 renders all frames", None))
#endif // QT_CONFIG(whatsthis)
        self.degreeLabel.setText(QCoreApplication.translate("lazySiouxsie", u"\u00b0", None))
        self.label.setText(QCoreApplication.translate("lazySiouxsie", u"Render Format", None))
        self.render_format.setItemText(0, QCoreApplication.translate("lazySiouxsie", u"png", None))
        self.render_format.setItemText(1, QCoreApplication.translate("lazySiouxsie", u"jpg", None))
        self.render_format.setItemText(2, QCoreApplication.translate("lazySiouxsie", u"exr", None))

        self.quality_label.setText(QCoreApplication.translate("lazySiouxsie", u"Quality", None))
#if QT_CONFIG(tooltip)
        self.quality_slider.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.quality_slider.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.quality_slider.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.quality_value.setToolTip(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.quality_value.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.quality_value.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"The quality setting for the renderer.  ", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.scene_lights.setToolTip(QCoreApplication.translate("lazySiouxsie", u"When checked, any lights created in the scene will be rendered as one of the render passes.  Otherwise the existing lights will be ignored.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.scene_lights.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"When checked, any lights created in the scene will be rendered as one of the render passes.  Otherwise the existing lights will be ignored.", None))
#endif // QT_CONFIG(statustip)
        self.scene_lights.setText(QCoreApplication.translate("lazySiouxsie", u"Use Scene Lights", None))
#if QT_CONFIG(tooltip)
        self.ground_plane.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Create a shadow catching ground plane", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.ground_plane.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Create a shadow catching ground plane", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.ground_plane.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Create a shadow catching ground plane", None))
#endif // QT_CONFIG(whatsthis)
        self.ground_plane.setText(QCoreApplication.translate("lazySiouxsie", u"Ground Plane", None))
#if QT_CONFIG(tooltip)
        self.chrome_balls.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Automatically generate Chrome and 50% Gray Spheres", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.chrome_balls.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Automatically generate Chrome and 50% Gray Spheres", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.chrome_balls.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Automatically generate Chrome and 50% Gray Spheres", None))
#endif // QT_CONFIG(whatsthis)
        self.chrome_balls.setText(QCoreApplication.translate("lazySiouxsie", u"Auto Chrome Balls", None))
        self.open_turntable.setText(QCoreApplication.translate("lazySiouxsie", u"Open Turntable File When Finished", None))
        self.submit_to_deadline.setText(QCoreApplication.translate("lazySiouxsie", u"Submit to Deadline", None))
        self.status_label.setText(QCoreApplication.translate("lazySiouxsie", u"Ready...", None))
        self.cancel_btn.setText(QCoreApplication.translate("lazySiouxsie", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.spin_btn.setToolTip(QCoreApplication.translate("lazySiouxsie", u"Create the Turnable file and submit it.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spin_btn.setStatusTip(QCoreApplication.translate("lazySiouxsie", u"Create the Turnable file and submit it.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.spin_btn.setWhatsThis(QCoreApplication.translate("lazySiouxsie", u"Create the Turnable file and submit it.", None))
#endif // QT_CONFIG(whatsthis)
        self.spin_btn.setText(QCoreApplication.translate("lazySiouxsie", u"Spin It", None))
    # retranslateUi

