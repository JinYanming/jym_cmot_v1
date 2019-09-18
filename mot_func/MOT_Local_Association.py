import numpy as np
from Common.list2array import lists2array
from Common.Idx2Types import Idx2Types
from Obj.Obs_Graph import Obs_Graph
from Obj.Obs_info import Obs_info
from Obj.Tracklet import Tracklet
from Obj.Z_item import Z_item

from tools.ListGiant import *
from mot_func.mot_appearance_model_generation import mot_appearance_model_generation
from mot_func.mot_eval_association_matrix import mot_eval_association_matrix
from mot_func.mot_association_hungarian import mot_association_hungarian


def MOT_Local_Association(Trk = None,detections = None,Obs_grap = None,param = None,fr = None,rgbimg = None,nargout1 = None,*args,**kwargs):
    ILDA  =  param.ILDA
    
    Z_meas = detections[fr]#represent the detections in current frame
    Z_meas = [detection[2:6] for detection in Z_meas]#choose the location(x,y,w,h) from raw data 
    ystates_ids = [detection[1] for detection in detections[fr]]
    ystate = Z_meas
    obs_grap = Obs_Graph()
    Obs_grap.append(obs_grap)
    Obs_grap[fr].iso_idx  =  np.ones((len(detections[fr])))
    obs_info = Obs_info()
    obs_info.ystate  =  []
    obs_info.yhist  =  []
    obs_info.ystates_ids = []
    if ~(np.all(ystate == 0)):
        yhist = mot_appearance_model_generation(rgbimg,param,ystate,True)#get the apperance model of the detections in current frame
        obs_info.ystate  =  ystate
        obs_info.yhist  =  yhist
        obs_info.ystates_ids = ystates_ids
        tidx,_,_ = Idx2Types(Trk,'High')#return the index of high confidence Tracklet
        yidx = np.where(Obs_grap[fr].iso_idx  ==  1)[0]#return the index of detections in current frame
        if len(tidx) != 0 and len(yidx) != 0:
            Trk_high = []
            Z_set = []
            trk_label = []
            conf_set = []
            #to generate a list of high confidence tracklet
            for ii in range(0,len(tidx)):
                i = tidx[ii]
                temp_Trk_high = Tracklet()
                temp_Trk_high.hist  =  Trk[i].A_Model
                temp_Trk_high.FMotion  =  Trk[i].FMotion
                temp_Trk_high.last_update  =  Trk[i].last_update
                temp_Trk_high.h  =  Trk[i].state[-1][3]
                temp_Trk_high.w  =  Trk[i].state[-1][2]
                temp_Trk_high.type  =  Trk[i].type
                Trk_high.append(temp_Trk_high)
                trk_label.append(Trk[i].label)
                conf_set.append(Trk[i].Conf_prob)
            # For detections in current frame
            meas_label = []
            for jj in range(0,len(yidx)):
                j = yidx[jj]#get the index of the j detection of detections in current frames 
                z_item = Z_item()#generate a object in order to record every detection's information include x,y,w,h, and Apperance model
                z_item.hist  =  yhist[:,:,j]
                z_item.pos  =  [ystate[j][0],ystate[j][1]]
                z_item.h  =  ystate[j][3]
                z_item.w  =  ystate[j][2]
                Z_set.append(z_item)
                meas_label.append(j)
            thr = param.obs_thr
            #generate the score matrix between Tracklet with high confidence and Detections in current frame

            score_mat = mot_eval_association_matrix(Trk_high,Z_set,param,'Obs',ILDA)
            confidence = []
            for i in Trk:
                confidence.append(i.Conf_prob)
            print(score_mat)
            #matching by hungarian Algorithm the the socre matrix shape should be[len(high_trk),len(high_trk]
            matching,__ = mot_association_hungarian(score_mat,thr,nargout = 2)
            print(matching)
            if matching.size != 0:
                for i in range(0,matching.shape[1]):
                    ass_idx_row = matching[0,i]
                    ta_idx = tidx[ass_idx_row]
                    ass_idx_col = matching[1,i]
                    ya_idx = yidx[ass_idx_col]
                    ListInsert(Trk[ta_idx].hyp.score,fr,score_mat[matching[0,i],matching[1,i]],0)
                    ListInsert(Trk[ta_idx].hyp.ystate,fr,ystate[ya_idx],[])
                    ListInsert(Trk[ta_idx].hyp.ystates_ids,fr,ystates_ids[ya_idx],-1)
                    
                    #Trk[ta_idx].hyp.score.append(score_mat[matching[0,i],matching[1,i]])
                    #Trk[ta_idx].hyp.ystate.append(ystate[ya_idx])
                    Trk[ta_idx].hyp.new_tmpl  =  yhist[:,:,ya_idx]
                    Trk[ta_idx].last_update  =  fr
                    Obs_grap[fr].iso_idx[ya_idx] = 0
    
    return Trk,Obs_grap,obs_info
    
if __name__  ==  '__main__':
    pass
    

