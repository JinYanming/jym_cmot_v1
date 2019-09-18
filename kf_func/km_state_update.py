import numpy as np
from Common.estimation_size import estimation_size
from kf_func.km_estimation import km_estimation
def km_state_update(Trk=None,ymeas=None,param=None,fr=None,*args,**kwargs):

    
    size_state=estimation_size(Trk,ymeas,fr)
    XX=Trk.FMotion.X[:,-1]
    PP=Trk.FMotion.P[:,:,-1]
    if len(ymeas) != 0:
        XX,PP=km_estimation(XX,ymeas[0:2],param,PP)
    else:
        XX,PP=km_estimation(XX,[],param,PP)
    
    pos_state = np.r_[XX[0],XX[2]]
    current_state = np.r_[pos_state[:,np.newaxis],size_state[:,np.newaxis]].squeeze()
    Trk.state.append(current_state)
    Trk.FMotion.X =  np.c_[Trk.FMotion.X,XX]
    Trk.FMotion.P = np.concatenate((Trk.FMotion.P,PP),axis = 2)
    return Trk
