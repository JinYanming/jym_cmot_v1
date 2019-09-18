import numpy as np
from Common.Idx2Types import Idx2Types
from Obj.Tracklet import Tracklet
from mot_func.mot_appearance_model_generation import mot_appearance_model_generation
from mot_func.mot_eval_association_matrix import mot_eval_association_matrix
from mot_func.mot_association_hungarian import mot_association_hungarian
from mot_func.mot_motion_model_generation import mot_motion_model_generation

from Obj.Z_item import Z_item
def MOT_Global_Association(Trk = None,Obs_grap = None,Obs_info = None,param = None,fr = None,*args,**kwargs):

    ILDA  =  param.ILDA
    Refer = []
    Test = []
    all_indx = [i for i in range(0,len(Trk))]
    low_indx,_,_ = Idx2Types(Trk,'Low')
    high_indx = np.setdiff1d(all_indx,low_indx)
    yidx = np.where(Obs_grap[fr].iso_idx  ==  1)[0]
    yhist = Obs_info.yhist
    ystate = Obs_info.ystate
    ystates_ids = Obs_info.ystates_ids
    High_trk = []
    Low_trk = []
    Y_set = []
    if len(low_indx) !=0:
        # For tracklets with low confidence
        for ii in range(0,len(low_indx)):
            i = low_indx[ii]
            temp_Trk_low = Tracklet()
            temp_Trk_low.hist  =  Trk[i].A_Model
            temp_Trk_low.FMotion  =  Trk[i].FMotion
            temp_Trk_low.last_update  =  Trk[i].last_update
            temp_Trk_low.h  =  Trk[i].state[-1][3]
            temp_Trk_low.w  =  Trk[i].state[-1][2]
            temp_Trk_low.type  =  Trk[i].type
            temp_Trk_low.end_time = Trk[i].efr
            Low_trk.append(temp_Trk_low)
        # For tracklet with high confidence
        for jj in range(0,len(high_indx)):
            j = high_indx[jj]
            temp_Trk_high = Tracklet()
            temp_Trk_high.hist  =  Trk[j].A_Model
            temp_Trk_high.h  =  Trk[j].state[-1][3]
            temp_Trk_high.w  =  Trk[j].state[-1][2]
            temp_Trk_high.FMotion  =  Trk[j].FMotion
            XX,PP = mot_motion_model_generation(Trk[j],param,'Backward',nargout = 2)
            temp_Trk_high.BMotion.X  =  XX
            temp_Trk_high.BMotion.P  =  PP
            temp_Trk_high.last_update  =  Trk[j].last_update
            temp_Trk_high.init_time  =  Trk[j].ifr
            High_trk.append(temp_Trk_high)
        iso_label = []
        if len(yidx) != 0:
            # For detections
            for jj in range(0,len(yidx)):
                j = yidx[jj]
                temp_y_set = Z_item()
                temp_y_set.hist  =  yhist[:,:,j]
                temp_y_set.pos  =  [ystate[j][0],ystate[j][1]]
                temp_y_set.h  =  ystate[j][3]
                temp_y_set.w  =  ystate[j][2]
                Y_set.append(temp_y_set)
                iso_label = j
        thr = param.obs_thr
        score_trk = mot_eval_association_matrix(Low_trk,High_trk,param,'Trk',ILDA)
        score_obs = mot_eval_association_matrix(Low_trk,Y_set,param,'Obs',ILDA)
        score_mat = np.concatenate((score_trk,score_obs),axis=1)
        matching,Affinity = mot_association_hungarian(score_mat,thr,nargout = 2)
        alpha = param.alpha
        rm_idx = []
        for m in range(0,len(Affinity)):
            mat_idx = matching[1,m]
            if mat_idx <=  len(high_indx) - 1:
                t_idx = low_indx[matching[0,m]]
                y_idx = high_indx[matching[1,m]]
                Trk[y_idx].ifr  =  Trk[t_idx].ifr
                fr1 = Trk[t_idx].ifr
                fr2 = Trk[t_idx].efr
                for kk in range(fr1,fr2):
                    Trk[y_idx].state[kk] = Trk[t_idx].state[kk]
                numHyp = len(Trk[t_idx].hyp.score)
                for kk in range(fr1,numHyp):
                    Trk[y_idx].hyp.score[kk] = Trk[t_idx].hyp.score[kk]
                    Trk[y_idx].hyp.ystate[kk] = Trk[t_idx].hyp.ystate[kk]
                    Trk[y_idx].hyp.ystates_ids[kk] = Trk[t_idx].hyp.ystates_ids[kk]
                for kk in range(numHyp + 1,fr):
                    Trk[y_idx].hyp.score[kk] = param.init_prob
                    Trk[y_idx].hyp.ystate[kk] = []
                    Trk[y_idx].hyp.ystates_ids[kk] = -1
                Trk[y_idx].A_Model  =  alpha*Trk[t_idx].A_Model + (1 - alpha)*Trk[y_idx].A_Model
                XX = []
                numState = len(Trk[y_idx].state)
                XX[1,:] = Trk(y_idx).state[fr1](1)
                XX[3,:] = Trk(y_idx).state[fr1](2)
                XX[2,:] = 0
                XX[4,:] = 0
                PP = param.P
                for ff in range(fr1,numState):
                    tState = Trk(y_idx).state[ff]
                    if logical_not(isempty(tState)):
                        XX,PP = km_estimation(XX,tState(range(1,2)),param,PP,nargout = 2)
                    else:
                        tState = Trk(y_idx).state[fr2]
                        XX,PP = km_estimation(XX,[],param,PP,nargout = 2)
                        Trk(y_idx).state[ff][range(1,2),:] = concat([[XX(1)],[XX(3)]])
                        Trk(y_idx).state[ff][range(3,4),:] = concat([[tState(1)],[tState(3)]])
                    Trk(y_idx).FMotion.X[:,ff] = XX
                    Trk(y_idx).FMotion.P[:,:,ff] = PP
                Trk(y_idx).label  =  copy(Trk[t_idx].label)
                Trk(y_idx).type  =  copy('High')
                rm_idx = concat([rm_idx,t_idx])
            else:
                m_idx = matching[1,m] - len(high_indx)
                t_idx = low_indx[matching[0,m]]
                y_idx = yidx[m_idx]
                for i in range(len(Trk[t_idx].hyp.score),fr):
                    Trk[t_idx].hyp.score.append(0)
                    Trk[t_idx].hyp.ystate.append([])
                    Trk[t_idx].hyp.ystates_ids.append(-1)
                Trk[t_idx].hyp.score.append(Affinity[m])
                Trk[t_idx].hyp.ystate.append(ystate[y_idx])
                Trk[t_idx].hyp.ystates_ids.append(ystates_ids[y_idx])
                Trk[t_idx].hyp.new_tmpl  =  yhist[:,:,y_idx]
                Trk[t_idx].last_update  =  fr
                Obs_grap[fr].iso_idx[y_idx] = 0
        if len(rm_idx) != 0:
            Trk[rm_idx] = []
    
    return Trk,Obs_grap
    
if __name__=='__main__':
    pass
    
