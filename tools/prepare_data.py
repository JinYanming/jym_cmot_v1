import os
import sys
import numpy as np
base_dir = "/workspace/MOT/jym_cmot"
sys.path.append(base_dir)
from config import Config
def get_sub_files(rootdir,param):    
    sub_files = []    
    for root, dirs, files in os.walk(rootdir,topdown = True):
        for name in files: 
            _, ending = os.path.splitext(name)
            if ending == param.imgtype:
                sub_files.append(name)   
    return sub_files
def prepare_data(param):
    ##### path config

    if param.use_gt_detections == False:
        det_file = open(param.dataset_path+"/det/det.txt")
    else:
        det_file = open(param.dataset_path+"/gt/gt.txt")
    detlines = det_file.readlines()
    detections = []
    fr_detections = []
    cur_det = 1
    #count object numbers 
    object_id_list = []
    deal = lambda x:x.strip("\n").split(",")#seperate the lines with ", " and remove the "\n"
    str2float = lambda x:[float(i) for i in x]
    ###get detections
    for detection in detlines:
        detection = deal(detection)[:-1]
        detection = str2float(detection)
        detection[2] = detection[2]-1
        detection[3] = detection[3]-1
        if detection[1] not in object_id_list:
            object_id_list.append(detection[1])
        if detection[0] == cur_det:
            fr_detections.append(detection[:7])
        else:
            detections.append(fr_detections)
            fr_detections = []
            fr_detections.append(detection[:7])
            cur_det = detection[0]
    param.detections = detections
    param.object_count = len(object_id_list)
    det_file.close()
    img_dir = param.dataset_path+"/img1"
    #img_list = get_sub_files(img_dir,param)
    img_list = []
    for i in range(0,param.imgSeq_lenth):
        imgName = "image_"+"{:08d}".format(i)+"_0"+param.imgtype
        img_list.append(imgName)
    param.img_List = img_list
    param.imgSeq_lenth = len(img_list)
    print("frames: {} detections:{} ||||img_list generate over!".format(len(param.img_List),len(detections)))
if __name__ == '__main__':
    param = Config()
    prepare_data(param)
