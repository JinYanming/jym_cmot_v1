import os
import cv2
import numpy as np
import operator
from functools import cmp_to_key
path = './result/'
filelist = os.listdir(path)

fps = 12 #视频每秒24帧
size = (640, 480) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改
video = cv2.VideoWriter("TrackResult.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)
#视频保存在当前目录下
imgList  = [img for img in filelist]
getId = lambda imgName:int(imgName[-14:-6])
imgList = sorted(imgList,key=cmp_to_key(lambda x,y:getId(x) - getId(y)))
for item in imgList:
    if item.endswith('.png'): 
    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
