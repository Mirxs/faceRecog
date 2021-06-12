#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, Response, request, jsonify,render_template
import redis
import face_recognition
import numpy as np
import pickle

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

# 首页
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#选择方式页面
@app.route('/choose', methods=['GET'])
def choose():
    return render_template('choose.html')

# 单张人脸录入页
@app.route('/upload', methods=['GET'])
def uploadHtml():
    return render_template('upload.html')

# 多张人脸录入页
@app.route('/upload1', methods=['GET'])
def uploadHtml1():
    return render_template('upload1.html')

# 单张人脸录入
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'code': 500, 'msg': '没有文件'})
    #获取文件流
    file = request.files['file']
    #获取文件名
    name = request.form['name']
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) != 1:
        return jsonify({'code': 500, 'msg': '该照片上不存在人脸'})
    face_encodings = face_recognition.face_encodings(image, face_locations)
    # 连数据库
    r = redis.Redis(connection_pool=pool)
    # 录入人名-对应特征向量
    r.set(name, face_encodings[0].tobytes())
    return jsonify({'code': 0, 'msg': '录入成功'})

# 多张人脸录入
@app.route('/upload1', methods=['POST'])
def upload1():
    fs=request.files.getlist('files')#文件列表
    name = []
    face_encodings = []
    for f in fs:
        name.append(f.filename.split('.')[0]) #获取文件名
        image = face_recognition.load_image_file(f)#获取图像
        face_locations = face_recognition.face_locations(image,model="cnn")#获取面部位置
        face_encodings.append(face_recognition.face_encodings(image, face_locations))#获取面部编码

    # 连数据库
    r = redis.Redis(connection_pool=pool)
    # 录入人名-对应特征向量
    for n ,face_encoding in zip(name,face_encodings):
        r.set(n, face_encoding[0].tobytes()) #默认一张图只有一张人脸
    return jsonify({'code': 0, 'msg': '录入成功'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)