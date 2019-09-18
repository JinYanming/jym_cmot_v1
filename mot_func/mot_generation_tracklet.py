import numpy as np
from mot_func.mot_return_ass_idx import mot_return_ass_idx
from mot_func.mot_search_association import mot_search_association
from mot_func.mot_tracklets_components_setup import mot_tracklets_components_setup
def mot_generation_tracklet(rgbimg=None,Trk=None,Obs_grap=None,detections=None,param=None,Y_set=None,fr=None,*args,**kwargs):

    
    ct=0
    non_iso=[]
    new_thr=param.new_thr
    for i in range(0,len(Y_set[fr].child)):
        prt_idx=Y_set[fr].child[i]
        if len(prt_idx) != 0:
            child_idx=mot_search_association(Y_set,fr,prt_idx)
            ass_idx=mot_return_ass_idx(child_idx,prt_idx,i,fr)
        else:
            child_idx=[]
            tmp_ass_idx=[]
            ass_ln=[]
            for j in range(0,len(prt_idx)):
                child_idx.append(mot_search_association(Y_set,fr,prt_idx))
                tmp_ass_idx.append(mot_return_ass_idx(child_idx[j],prt_idx,i,fr))
                ass_ln.append(len(np.where(tmp_ass_idx[j] != 0)))
            pid=np.max(ass_ln)
            ass_idx=tmp_ass_idx[pid]
        if len(np.where(np.array(ass_idx) != -1)[0]) >= new_thr:
            ct=ct + 1
            Trk,param=mot_tracklets_components_setup(rgbimg,Trk,detections,fr+1,ass_idx,param,None)
            idx=[]
            nT=len(np.where(np.array(ass_idx) != -1)[0])
            for h in range(0,nT):
                idx1=np.where(Obs_grap[fr + h - nT + 1].iso_idx == 1)[0]
                idx2=idx1[ass_idx[-1 + h - nT + 1][0]]
                idx.append(idx2)
            non_iso = non_iso + idx
    for j in range(0,len(non_iso)):
        setr=non_iso[j]
        if Obs_grap[fr + j - nT+1].iso_idx[setr] == 0:
            puase
        Obs_grap[fr + j - nT+1].iso_idx[setr] = 0
    
    
    return Trk,param,Obs_grap
    
if __name__ == '__main__':
    pass
    

