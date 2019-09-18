import numpy as np
from Obj.Tracklet import Tracklet
from Common.Labelling import Labelling
from tools.ListGiant import ListInsert
from mot_func.mot_motion_model_generation import mot_motion_model_generation
from mot_func.mot_appearance_model_generation import mot_appearance_model_generation
def mot_tracklets_components_setup(img=None,Trk=None,detections=None,cfr=None,y_idx=None,param=None,tmp_label=None,initTracklet = False,*args,**kwargs):
    #y_idx the tracklet state
    ass_idx=y_idx
    nofa=len(np.where(np.array(y_idx) != -1)[0])
    #record the detections id which refer to the object
    ystate_id_list = []
    tracklet = Tracklet()#genenrate a new tracklet
    tracklet.Conf_prob = param.init_prob
    tracklet.type = 'High'
    tracklet.reliable = 'False'
    tracklet.isnew = 1
    tracklet.sub_img = []
    tracklet.status = 'none'
    if tmp_label != None :
        tracklet.label = tmp_label
    else:
        param,idx=Labelling(param)
        tracklet.label = idx
    
    tracklet.ifr = cfr - nofa
    tracklet.efr = 0
    tracklet.last_update = cfr - 1
    Acc_tmpl = np.zeros(((param.Bin*3),param.subregion))
    for i in range(0,nofa):#from crruent frame to  track the len(ass_idx) privious frames detections
        state = np.array((4))
        tmp_idx=cfr - i -1
        temp_state = np.array(detections[tmp_idx][ass_idx[tmp_idx][0]][2:6].copy())
        ystate_id_list.append(detections[tmp_idx][ass_idx[tmp_idx][0]][1])
        ListInsert(tracklet.state,tmp_idx,temp_state,[])
        #tracklet.state.append(temp_state)
        #tracklet.state[tmp_idx][3,1]=detections(tmp_idx).h(ass_idx(tmp_idx))
        tmpl=mot_appearance_model_generation(img[tmp_idx],param,temp_state,False)
        Acc_tmpl=Acc_tmpl + tmpl.squeeze()[:,np.newaxis]
    
    ystate_id_list.reverse()
    
    # Appearnce Model
    tracklet.A_Model = Acc_tmpl / nofa
    # Forward Motion Model
    # XX [4,frames]
    XX,PP=mot_motion_model_generation(tracklet,param,'Forward',nargout=2)
    lt=XX.shape[1]
    tracklet.FMotion.X = np.zeros((4,cfr))
    tracklet.FMotion.P = np.zeros((4,4,cfr))
    tracklet.FMotion.X[:,cfr -lt:]=XX
    tracklet.FMotion.P[:,:,cfr - lt:]=PP
    tracklet.BMotion.X = []
    tracklet.BMotion.P = []
    tracklet.hyp.score = [0]*cfr
    tracklet.hyp.ystate = [item for item in tracklet.state]
    tracklet.hyp.ystates_ids = ystate_id_list
    Trk.append(tracklet)
    #count the number of the total tracklets
    param.total_tracklet_count += 1
    return Trk,param
    
if __name__ == '__main__':
    pass
    

