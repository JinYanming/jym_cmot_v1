import numpy as np
from tools.ListGiant import ListIndice2d
def estimation_size(Trk=None,ystate=None,fr=None,*args,**kwargs):

    
    init_time=Trk.ifr
    nof_s=4
    sum_size=Trk.state[-1][2:4]
    if fr == Trk.last_update:
        size_state=ystate[2:4]
    else:
        if fr > init_time + 3:
            for j in range(0,nof_s):
                sum_size=sum_size + Trk.state[-1-j][2:]
            size_state=sum_size / (nof_s + 1)
        else:
            all_est=Trk.state
            all_est=np.array(Trk.state)
            print(all_est.shape)
            all_est_select=ListIndice2d(all_est,None,[2,4])
            sum_size=sum_size + np.sum(all_est,0)
            size_state=sum_size / (size(all_est,2) + 1)
    return np.array(size_state)
    
if __name__ == '__main__':
    pass
    
