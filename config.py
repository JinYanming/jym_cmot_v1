import numpy as np
import os
class Config(object):
    def __init__(self):
        ####
        self.object_count = 0
        self.total_tracklet_count = 0
        self.ids = 0
        ####
        self.imgSeq_lenth = 400
        ###
        self.draw_while_track = True
        self.xy_center = True
        self.use_gt_detections = False
        ##get detections
        self.detections = None
        ## Get image lists
        #self.dataset_path = '/data/dataset/MOT/MOT17/train/MOT17-02-FRCNN'
        self.dataset_path = '/data/dataset/MOT/ETH'
        self.img_path = self.dataset_path+'/img1/'
        self.img_List = None
        #self.imgsize = [1920,1080,3]
        self.imgsize = [480,640,3]
        self.imgtype = ".png"
        

        ## Common selfeter
        self.label = np.array([0]*10000)
        self.show_scan = 4
        self.new_thr = self.show_scan + 1    # Temporal window size for tracklet initialization
        self.obs_thr = 0.4                    # Threshold for local and global association
        self.type_thr = 0.5                   # Threshold for changing a tracklet type
        self.pos_var = np.diag([30**2,75**2])      # Covariance used for motion affinity evalutation
        self.alpha = 0.2

        ## Tracklet confidence 
        self.lambda_ = 1.2
        self.atten = 0.85
        self.init_prob = 0.75                 # Initial confidence 

        ## Appearance Model 
        self.tmplsize = [64, 32]                           # template size (height, width)
        self.Bin = 48                                      # # of Histogram Bin
        self.vecsize = self.tmplsize[0]*self.tmplsize[1]
        self.subregion = 1
        self.subvec = int(self.vecsize/self.subregion)
        self.color = 'RGB'                            # RGB or HSV



        ## Motion model  
        # kalman filter selfeter
        self.Ts = 1 # Frame rates

        self.Ts = self.Ts
        self.F1 = np.array([[1,self.Ts],[0,1]])
        self.Fz = np.zeros((2,2)) 
        self.F = np.array(np.r_[np.c_[self.F1,self.Fz],np.c_[self.Fz,self.F1]]) # F matrix: state transition matrix

        # Dynamic model covariance
        self.q= 0.05 

        self.Q1 = np.array([[self.Ts**4,self.Ts**2],[self.Ts**2,self.Ts]])*self.q**2
        self.Q = np.array(np.r_[np.c_[self.Q1,self.Fz],np.c_[self.Fz,self.Q1]]) 

        # Initial Error Covariance
        ppp = 5
        self.P = np.diag([ppp,ppp,ppp,ppp]) 
        self.H = np.array([[1,0,0,0],[0,0,1,0]]) # H matrix: measurement model
        self.R = 0.1*np.identity(2) # Measurement model covariance

        class ilda(object):
            def __init__(self):
                pass
        ## ILDA selfeters
        self.ILDA = ilda()
        self.use_ILDA = 1 # 1:ILDA, 0: No-ILDA
        self.ILDA.n_update = 0  
        self.ILDA.eigenThreshold = 0.01 
        self.ILDA.up_ratio = 3  
        self.ILDA.duration = 5
        self.ILDA.feat_data = []
        self.ILDA.feat_label = []
        self.colormap=np.array([
                [0,0,0.75],
                [0,0,1],
                [0,0.25,1],
                [0,0.5,1],
                [0,0.75,1],
                [0,1,1],
                [0.25,1,0.75],
                [0.5,1,0.75],
                [0.75,1,0.25],
                [1,1,0],
                [1,0.75,0],
                [1,0.5,0],
                [1,0.25,0],
                [1,0,0,],
                [0.75,0,0],
                [0.5,0,0]
                ]
                )




