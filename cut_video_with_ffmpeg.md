# 用ffmpeg截取视频
## 精确方式
ffmpeg -ss [start] -t [duration] -i [in].mp4  -c:v libx264 -c:a aac -strict experimental -b:a 98k [out].mp4
## 非精确方式
ffmpeg -ss [start] -t [duration] -accurate_seek -i [in].mp4 -codec copy  -avoid_negative_ts 1 [out].mp4
## 去掉视频中的音轨
ffmpeg -i mavel4.mp4 -vcodec copy -an mav.mp4
## 截取视频a
ffmpeg -ss 00:01:00 -i in.mp4 -to 00:01:10 -acodec copy -copyts out.mp4


## 第二种方法
简单命令
    ffmpeg -i input.mp4 -ss 1:05 -t 10 output.mp4 

快速方法
    ffmpeg -ss 1:05 -i input.mp4 -t 10 -c:v copy -c:a copy output.mp4
    把-ss 1:05放到-i前面，与原来的区别是，这样会先跳转到第1:05秒在开始解码输入视频，而原来的会从开始解码，只是丢弃掉前1:05秒的结果。
-c:v 和 -c:a分别指定视频和音频的编码格式。
-c:v copy -c:a copy标示视频与音频的编码不发生改变，而是直接复制，这样会大大提升
