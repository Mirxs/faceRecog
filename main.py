#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PIL import Image
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal, QUrl
from PyQt5.QtGui import QKeyEvent, QTextCursor
import matplotlib.pyplot as plt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# 导入qt designer生成的Ui_widget模块
from window import Ui_Form

# 导入findFace模块
from findFace import FindFace


def tran(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return (h, m, s)
# 结果窗口


# class ChildWindow(QMainWindow, Ui_result):
#     def __int__(self, parent):
#         """
#         一个新窗口，用于显示结果截图的放大版本
#         Args:
#         image_file：传入的文件地址

#         """
#         super(ChildWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.parent = parent
#         # 设置图片尺寸自适应
#         self.big_result_label.setScaledContents(True)
#         # 显示图片
#         png = QtGui.QPixmap(self.parent.result_image)
#         self.big_result_label.setPixmap(png)


class Stream(QObject):
    """重定向控制台输出到pyqt5组件"""
    newText = pyqtSignal(str)  # 自定义信号

    def write(self, text):
        self.newText.emit(str(text))  # 发射信号
        QApplication.processEvents()  # 实时显示控制台输出


class MainForm(QMainWindow, Ui_Form):
    """主界面"""
    def __init__(self, parent=None):
        # 运行结束标志
        self.flag = False

        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        # 选择视频文件按钮事件
        self.video_button.clicked.connect(self.open_file)
        # 选择图片按钮绑定事件
        self.photo_button.clicked.connect(self.open_file)

        # 开始按键绑定事件
        self.begin_button.clicked.connect(self.begin)
        # 播放视频按钮绑定事件
        self.play_video.clicked.connect(self.playVideo)
        # 输入的视频和图片路径
        self.input_movie = None
        self.input_image = None

        # 确保光标可见
        self.output_text.ensureCursorVisible()
        # 自定义输出流
        sys.stdout = Stream(newText=self.onUpdateText)

        # 播放器
        self.player = QMediaPlayer()
        # 设置播放组件
        self.player.setVideoOutput(self.video_widget)

        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.slider_video.sliderMoved.connect(self.updatePosition)
        # 设置图片尺寸自适应
        # self.label_img.setScaledContents(True)
        self.label_result.setScaledContents(True)

        # 结果listWidget点击绑定事件
        self.image_list.itemClicked.connect(self.displayResultImages)

        # 结果文件保存路径
        self.dir = None

        # 放大截图按钮，显示大图
        self.show_big_button.clicked.connect(self.showBigResultImage)
        # # 子窗口
        # self.resultWindow = ChildWindow(parent=self)

        self.result_image = None

        #结果框水平滑动条
        self.output_text.setLineWrapMode(QtWidgets.QTextBrowser.NoWrap)
        self.output_text.horizontalScrollBar().setValue(0)

        #获取焦点以防止空格键失效
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        #查找类
        self.face_rec = None

    # 更新输出文本框
    def onUpdateText(self, text):
        """输出写入到texture中"""
        cursor = self.output_text.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.output_text.setTextCursor(cursor)
        self.output_text.ensureCursorVisible()

    def closeEvent(self, event):
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    # 打开文件
    def open_file(self):
        button = self.sender()  # 获取信号源头
        filename, filetype = QFileDialog.getOpenFileName(self, "选择文件",

                                                         '.', filter="Video&Images(*.webm *avi *mp4 *.jpg *png)")
        if button.objectName() == "video_button":  # 如果是视频
            self.file0_text.clear()  # 清除原有的文字
            self.input_movie = filename
            if filename != '':
                self.file0_text.append(
                    "已经{}：{}".format(button.text(), filename))
                # 设置为播放媒体
                self.player.setMedia(QMediaContent(
                    QUrl.fromLocalFile(self.input_movie)))
            else:
                self.file0_text.append("您没有选择任何文件")
        else:  # 如果是图片
            self.file1_text.clear()  # 清除原有的文字
            self.input_image = filename
            # print(self.input_image)
            if filename != '':
                self.file1_text.append(
                    "已经{}：{}".format(button.text(), filename))
                # 显示图片
                png = QtGui.QPixmap(self.input_image)
                scaledPng=png.scaled(self.label_img.size(),QtCore.Qt.KeepAspectRatio) #保持比例缩放
                self.label_img.setPixmap(scaledPng)

            else:
                self.file1_text.append("您没有选择任何文件")

    # 开始处理

    def begin(self):
        self.clearResultList()
        if self.isValid():
            self.begin_button.setEnabled(False)  # 设置按钮不可用
            self.output_text.clear()  # 清除输出框
            self.face_rec = FindFace(self.input_movie, self.input_image)  # 初始化Findface对象
            print("正在查找输入图片上的人脸")
            #照片上没有人脸
            if not self.face_rec.isHaveFace():
                self.begin_button.setEnabled(True)  # 设置按钮可用
                pass
            else:
                # self.begin_button.setEnabled(False)  # 设置按钮不可用
                self.dir = self.face_rec.get_face_from_video()  # 开始处理
                self.face_rec.release()  # 释放资源
                # 显示结果截图
                self.showResultList(self.dir)
                self.begin_button.setEnabled(True)  # 设置按钮可用
                self.flag = True

    # 播放视频

    def playVideo(self):
        # 设置媒体
        if self.player.state() == 1:
            print("视频已暂停播放")
            self.player.pause()
        else:
            print("视频已经开始播放")
            self.player.play()

    # 视频总时长获取
    def getDuration(self, d):
        '''d是视频时长（ms）'''
        self.slider_video.setRange(0, d)
        self.slider_video.setEnabled(True)
        # self.displayTime(d)

    # 视频实时位置获取
    def getPosition(self, p):
        self.slider_video.setValue(p)
        self.displayTime(p)
    # 用进度条更新视频位置

    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(v)

    def displayTime(self, ms):
        # 视频总时长
        duration = self.slider_video.maximum()
        duration_seconds = int(duration/1000)
        dh, dm, ds = tran(duration_seconds)

        seconds = int(ms/1000)
        h, m, s = tran(seconds)
        if h == 0 and m == 0 and s == 0:
            self.label_time.setText('--:--:--')
        else:
            self.label_time.setText('时间：                             '
                                    '                             {}:{}:{}/{}:{}:{}'.format(h, m, s, dh, dm, ds))

    # 显示结果列表
    def showResultList(self, dir):
        "dir为结果截图目录"
        # 打开水平和垂直的滚动条
        self.image_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.image_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        dir_list = os.listdir(dir)
        # 按创建时间对文件夹排序
        if not dir_list:
            return
        else:
            dir_list = sorted(
                dir_list, key=lambda x: os.path.getctime(os.path.join(dir, x)))
        for i in dir_list:
            self.image_list.addItem(i)

    # 显示结果图像列表
    def displayResultImages(self, item):
        self.result_image = self.dir+"/"+item.text()
        png = QtGui.QPixmap(self.result_image)
        scaledPng=png.scaled(self.label_img.size(),QtCore.Qt.KeepAspectRatio) #保持比例缩放
        self.label_result.setPixmap(scaledPng)
        self.label_result.setPixmap(png)
    
    #清空结果图像列表
    def clearResultList(self):
        # count = self.image_list.count()
        # for i in range(count):
        #     self.image_list.takeItem(i)
        while(self.image_list.count()!= 0):
            self.image_list.takeItem(0)

    # 用另外一个窗口显示放大的截图
    def showBigResultImage(self):
        if self.result_image is not None:
            im=Image.open(self.result_image)
            # im.show()
            plt.imshow(im)
            plt.show()
    
    #判断输入文件是否正确
    def isValid(self):
        if self.input_image ==None or self.input_movie == None:
            if self.input_image == None:
                print("没有输入图片！！！！")
            if self.input_movie == None:
                print("没有输入视频！！！！")
            return False
        if (not self.input_image.lower().endswith(('.jpg','.png'))) or (not self.input_movie.lower().endswith(('.webm','.avi','.mp4'))):
            if not self.input_image.lower().endswith(('.jpg','.png')):
                print("输入的不是图片文件！！！！（请输入以jpg、png为后缀名的图片）")
            if not self.input_movie.lower().endswith(('.webm','.avi','.mp4')):
                print("输入的不是视频文件！！！！（请输入 以webm、avi、mp4为后缀名的视频）")
            return False
        return True
    
    #空格按键按下事件
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == QtCore.Qt.Key_Space:
            self.playVideo()
        return super().keyPressEvent(a0)
if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
