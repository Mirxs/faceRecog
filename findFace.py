#!/usr/bin/python3
# -*- coding: utf-8 -*-


import face_recognition
import cv2
import math
import time
import shutil
import os

#把秒转化为时：分：秒格式

def tran(seconds):
    m,s =divmod(seconds,60)
    h,m =divmod(m,60)
    return (h,m,s)

class FindFace():
    """在视频中查找指定人脸

    Args:
    video:输入视频路径

    image：输入图片路径

    methods：
    show_video_info:显示视频信息

    get_face_from_video：在视频中查找人脸

    release：释放资源

    isHaveFace：判断输入照片中是否有人脸
    """

    def __init__(self, video: str, image:str):
        #输入文件具体路径
        self.video=video
        self.image=image
        self.video_name = os.path.split(video)[1] #返回文件名，接受最后一个参数
        self.image_name = os.path.split(image)[1]
        # 打开视频文件
        self.input_video = cv2.VideoCapture(video)
        self.frame_count = int(self.input_video.get(cv2.CAP_PROP_FRAME_COUNT)) # 总帧数
        self.frame_rate = math.ceil(self.input_video.get(cv2.CAP_PROP_FPS)) # 视频帧率
        self.frame_duration = int(self.frame_count/self.frame_rate)  # 视频长度（秒）


        # 加载要识别的人脸图片
        self.input_image = face_recognition.load_image_file(image)
        if len(face_recognition.face_encodings(self.input_image)) ==0:
            pass
        else:
            self.image_face_encoding = face_recognition.face_encodings(self.input_image)[0]

            # 初始化一些变量
            self.face_locations = []
            self.face_encodings = []
            # self.name = image.split('.')[0]  # 名字
            self.frame_number = 1
            self.know_faces = [self.image_face_encoding]

            # 写出文件
            # fourcc = cv2.VideoWriter_fourcc(*'XVID')
            # self.output_video = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))
        
    def show_video_info(self):
        """
        显示视频文件信息‘
        """
        h,m,s = tran(self.frame_duration)
        print("{}的长度为{}时{}分{}秒，帧率为{}".format(self.video,h,m,s,self.frame_rate))

        # time.sleep(3) # 暂停3秒

    def get_face_from_video(self):
        """
        在视频中查找人脸
        """
        #文件存储目录
        path0 = self.video_name.split(".")[0]
        path1 = self.image_name.split(".")[0]
        dir = "./photo/find_{}_in_{}".format(path1,path0)
        if os.path.exists(dir):
            shutil.rmtree(dir)
            #print("删除成功")
            os.mkdir(dir)
        else:
            os.mkdir(dir)
        self.show_video_info()

        #记录运行事件
        start_time = time.time()

        result = [] #结果
        while True:
            ret, frame = self.input_video.read()

            #每隔一秒扫描一下
            if self.frame_number%self.frame_rate != 1:
                self.frame_number+=1
                continue

            # 打印处理进度
            if self.frame_number/self.frame_count <=1.0 :
                percent = self.frame_number/self.frame_count
            else :
                percent = 1.0
            percent = self.frame_number/self.frame_count if self.frame_number/self.frame_count <=1.0 else 1.0

            print("处理进度为：{:.2%}".format(percent))

            # 当视频读处理完时退出
            if not ret:
                break

            # 将视频的BGR 转化为 RGB格式
            rgb_frame = frame[:, :, ::-1]

            # 找到当前帧的所有的脸和脸部编码
            self.face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
            self.face_encodings = face_recognition.face_encodings(rgb_frame, self.face_locations)

            # self.face_names = []
            
            #记录face_encoding在self.face_encodings中的位置
            index=0
            for face_encoding in self.face_encodings:
                # 与图片的脸匹配
                match = face_recognition.compare_faces(self.know_faces, face_encoding, tolerance=0.6)

                # 如果匹配上了,存储结果
                if match[0]:
                    #print("找到")
                    seconds=math.ceil(self.frame_number/self.frame_rate)
                    # # #减去一秒，为了匹配pyqt5的记时
                    # seconds=seconds-1
                    h,m,s = tran(seconds)
                    s=s-1
                    r=("{}:{}:{}".format(h,m,s))
                    r1=("在{}时{}分{}秒找到图片上的人脸".format(h,m,s))
                    print(r1)
                    result.append(r)
                    face_location = self.face_locations[index]
                    # 给脸画上边框
                    (top,right,bottom,left) = face_location
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    save_path="{}/{}.png".format(dir,r)
                    cv2.imwrite(save_path,frame)
                    # # 导出查找到后的截图,异常处理
                    # try:
                    #     #位置
                    #     i=self.face_encodings.index(face_encoding)
                    #     face_location = self.face_locations[i]
                    #     # 给脸画上边框
                    #     (top,right,bottom,left) = face_location
                    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    #     save_path="{}/{}.png".format(dir,r)
                    #     cv2.imwrite(save_path,frame)
                    # except Exception as ex:
                    #     print("在{}时{}分{}秒出现异常{}".format(h,m,s,ex))
                    #     continue
                    #     #位置
                    # 记录face_encoding在self.face_encodings中的位置




                # # 导出查找到后的截图
                # for (top, right, bottom, left) in self.face_locations:
                #     if not match[0]:  # 如果这帧没有找到,跳过这帧率
                #         continue
                #     else:
                #         # 给脸画上边框
                #         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                #         # 写上名字
                #         cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
                #         font = cv2.FONT_HERSHEY_DUPLEX
                #         cv2.putText(frame, self.name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)


                # # 将视频帧写入新的视频
                # self.output_video.write(frame)
                index = index+1
            self.frame_number += 1
        
        #结束时间
        end_time=time.time()

        #去掉结果中重复时间
        result={}.fromkeys(result).keys()

        #打印结果,每10个结果换一行
        ncount=10
        print("结果为：")
        
        count=ncount
        print("在视频{}出现图片{}中的人脸的时间点为：".format(self.video_name,self.image_name))
        for x in range(0,ncount-1):
            print("---------------------",end='')
        print()
        for x in result:
            if count == 1:
                count=ncount
                print(x.ljust(12))
            else:
                print(x.ljust(12),end="")
                count = count -1
        print()
        for x in range(0,ncount-1):
            print("---------------------",end='')
        print()
        #输出所用事件
        h,m,s = tran(int(end_time-start_time))
        print("共用时{}时{}分{}秒".format(h,m,s))

        #返回存储文件目录路径
        return dir


    # 释放视频
    def release(self):
        """
        释放资源
        """
        self.input_video.release()
        # self.output_video.release()
        print("已经处理完毕")
        cv2.destroyAllWindows()
    
    #判断照片上是否有人脸
    def isHaveFace(self):
        """
        判断照片中是否有人脸
        """
        if len(face_recognition.face_encodings(self.input_image)) ==0:
            print("输入的照片中没有人脸!!!")
            return False
        else:
            return True


if __name__ == "__main__":
    faceFind = FindFace("./resource/hamilton_clip.mp4", "./resource/lin-manuel-miranda.png")
    #faceFind = FindFace("./resource/testvideo3.mp4", "./resource/superman.jpg")
    faceFind.get_face_from_video()
    faceFind.release()
