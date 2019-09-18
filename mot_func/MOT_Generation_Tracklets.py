import numpy as np
from mot_func.mot_generation_tracklet import mot_generation_tracklet
from mot_func.mot_non_associated import mot_non_associated
from mot_func.mot_pre_association_tracking import mot_pre_association_tracking 
from Obj.ISO import ISO

def MOT_Generation_Tracklets(init_img_set=None,Trk=None,detections=None,param=None,Obs_grap=None,cfr=None,*args,**kwargs):

    
    st_fr=cfr - param.show_scan
    en_fr=cfr
    #use iso to record the unmatched detections in every frames
    iso =  ISO()
    iso.meas = []
    iso.node = []
    iso.ystates_ids = []
    iso=mot_non_associated(detections,Obs_grap,iso,st_fr,en_fr+1)
    iso=mot_pre_association_tracking(iso,st_fr,en_fr+1)
    Trk,param,Obs_grap=mot_generation_tracklet(init_img_set,Trk,Obs_grap,iso.meas,param,iso.node,cfr)
    print("length of Trk is :",len(Trk))
    
    return Trk ,param, Obs_grap
