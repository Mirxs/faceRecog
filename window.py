# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1245, 1000)
        Form.setMinimumSize(QtCore.QSize(1245, 1000))
        Form.setMaximumSize(QtCore.QSize(1245, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../resource/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.output_text = QtWidgets.QTextBrowser(Form)
        self.output_text.setGeometry(QtCore.QRect(540, 640, 601, 321))
        self.output_text.setObjectName("output_text")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(30, 960, 1131, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 10, 41, 961))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(30, 0, 1131, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(1145, 10, 31, 961))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.video_widget = QVideoWidget(Form)
        self.video_widget.setGeometry(QtCore.QRect(49, 99, 581, 441))
        self.video_widget.setObjectName("video_widget")
        self.label_time = QtWidgets.QLabel(Form)
        self.label_time.setGeometry(QtCore.QRect(50, 580, 571, 31))
        self.label_time.setObjectName("label_time")
        self.slider_video = QtWidgets.QSlider(Form)
        self.slider_video.setGeometry(QtCore.QRect(50, 550, 571, 18))
        self.slider_video.setOrientation(QtCore.Qt.Horizontal)
        self.slider_video.setObjectName("slider_video")
        self.label_img = QtWidgets.QLabel(Form)
        self.label_img.setGeometry(QtCore.QRect(650, 140, 481, 321))
        self.label_img.setObjectName("label_img")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(640, 90, 511, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(630, 100, 21, 411))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(640, 500, 511, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(30, 613, 1131, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(1140, 100, 20, 411))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 30, 511, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file1_text = QtWidgets.QTextBrowser(self.layoutWidget)
        self.file1_text.setObjectName("file1_text")
        self.horizontalLayout_2.addWidget(self.file1_text)
        self.photo_button = QtWidgets.QPushButton(self.layoutWidget)
        self.photo_button.setObjectName("photo_button")
        self.horizontalLayout_2.addWidget(self.photo_button)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 30, 581, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file0_text = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.file0_text.setObjectName("file0_text")
        self.horizontalLayout.addWidget(self.file0_text)
        self.video_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.video_button.setObjectName("video_button")
        self.horizontalLayout.addWidget(self.video_button)
        self.image_list = QtWidgets.QListWidget(Form)
        self.image_list.setGeometry(QtCore.QRect(40, 640, 121, 321))
        self.image_list.setObjectName("image_list")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(190, 660, 321, 271))
        self.label_result.setObjectName("label_result")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(170, 640, 16, 321))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_11 = QtWidgets.QFrame(Form)
        self.line_11.setGeometry(QtCore.QRect(520, 640, 16, 321))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Form)
        self.line_12.setGeometry(QtCore.QRect(180, 950, 351, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(Form)
        self.line_13.setGeometry(QtCore.QRect(180, 630, 351, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(710, 530, 391, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.begin_button = QtWidgets.QPushButton(self.widget)
        self.begin_button.setObjectName("begin_button")
        self.horizontalLayout_3.addWidget(self.begin_button)
        self.play_video = QtWidgets.QPushButton(self.widget)
        self.play_video.setObjectName("play_video")
        self.horizontalLayout_3.addWidget(self.play_video)
        self.show_big_button = QtWidgets.QPushButton(self.widget)
        self.show_big_button.setObjectName("show_big_button")
        self.horizontalLayout_3.addWidget(self.show_big_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸检索平台"))
        self.label_time.setText(_translate("Form", "时间"))
        self.label_img.setText(_translate("Form", "                                            待查找图片"))
        self.file1_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请选择输入的图片文件</p></body></html>"))
        self.photo_button.setText(_translate("Form", "选择照片"))
        self.file0_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请选择输入的视频文件</p></body></html>"))
        self.video_button.setText(_translate("Form", "选择视频"))
        self.label_result.setText(_translate("Form", "                            结果截图展示"))
        self.begin_button.setText(_translate("Form", "开始查找"))
        self.play_video.setText(_translate("Form", "播放/暂停"))
        self.show_big_button.setText(_translate("Form", "放大截图"))
from PyQt5.QtMultimediaWidgets import QVideoWidget