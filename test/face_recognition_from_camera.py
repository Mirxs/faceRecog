#!/usr/bin/python3
# -*- coding: utf-8 -*-


import face_recognition
from cv2 import cv2
import numpy as np
import redis
import pickle
# from PIL import Image, ImageDraw, ImageFont

# def cv2ImgAddText(img, text, left, bottom, textColor=(255, 255, 255), textSize=20):
#     if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
#         img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     draw = ImageDraw.Draw(img)
#     fontText = ImageFont.truetype(
#         "msyh.ttc", textSize, encoding="utf-8")
#     draw.text((left, bottom), text, textColor, font=fontText)
#     return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# 获取摄像头
video_capture = cv2.VideoCapture(0)
# 连数据库
r = redis.Redis(connection_pool=pool)
# 取出数据库中所有的人名和它对应的编码
known_face_names = r.keys()
known_face_encodings  = r.mget(known_face_names)
#读取数组库人脸编码和名字
known_face_encodings=[np.frombuffer(x) for x in known_face_encodings]
known_face_names=[str(x,'utf-8') for x in known_face_names]
# 初始化人脸位置，编码和名字
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 获取每一帧图像
    ret, frame = video_capture.read()

    # 将图像缩放为原来的1/4便于处理
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 从BGR转换为RGB格式
    rgb_small_frame = small_frame[:, :, ::-1]

    # 每隔一帧处理一帧图像以节省时间
    if process_this_frame:
        #使用卷积神经网络模型进行识别
        face_locations = face_recognition.face_locations(rgb_small_frame,model="cnn")
        #使用hog模型识别
        #face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 找到匹配的人脸
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.6)
            name = "Unknown"
            #找到距离最近的人脸
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    #显示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 确定人脸位置
        top =top*4
        right = right*4
        bottom = bottom*4
        left = left*4

        # 框出人脸
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 名字框
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        # name=''+str(name,encoding='utf-8')
        # frame = cv2ImgAddText(frame,name, left + 6, bottom - 6, (255, 255, 255), 20)
        
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)

    # 显示结果
    cv2.namedWindow('Face Recongnition',cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Face Recongnition',cv2.WND_PROP_AUTOSIZE,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Face Recongnition', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
video_capture.release()
#关闭窗口
cv2.destroyAllWindows()
