import numpy as np
from mot_func.mot_search_association import mot_search_association
from mot_func.mot_return_ass_idx import mot_return_ass_idx
from mot_func.mot_tracklets_components_setup import mot_tracklets_components_setup
def MOT_Initialization_Tracklets(rgbimg=None,Trk=None,detections=None,param=None,Y_set=None,fr=None,*args,**kwargs):
    print("MOT_Initialization_Tracklets.py start")
    fr = fr 
    new_thr=param.new_thr
    for i in range(0,len(Y_set[fr-1].child)):#backup to init the initial tracklet
        prt_idx=Y_set[fr-1].child[i]
        if len(prt_idx) <=1:
            child_idx=mot_search_association(Y_set,fr-1,prt_idx)#child_idx:the init tracklet
            ass_idx=mot_return_ass_idx(child_idx,prt_idx,i,fr-1)
        else:
            child_idx=[]
            tmp_ass_idx=[]
            ass_ln=[]
            for j in range(0,len(prt_idx)):
                child_idx[j]=mot_search_association(Y_set,fr-1,prt_idx(j))
                tmp_ass_idx[j]=mot_return_ass_idx(child_idx[j],prt_idx(j),i,fr-1)
                ass_ln[j]=len(find(tmp_ass_idx[j] != 0))
            __,pid=max(ass_ln)
            ass_idx=tmp_ass_idx[pid]
        if len(np.where(np.array(ass_idx) != -1)[0]) >= new_thr:#if the length of init tracketlet >4 then generate the tracklet
            Trk,param=mot_tracklets_components_setup(rgbimg,Trk,detections,fr,ass_idx,param,None,True)
            for h in range(0,len(np.where(ass_idx != 0))):
                Y_set[fr-1 - h].child[ass_idx[-1 - h][0]]=0
    
    print("MOT_Initialization_Tracklets over")
    return Trk,param,Y_set
    
if __name__ == '__main__':
    pass
    
