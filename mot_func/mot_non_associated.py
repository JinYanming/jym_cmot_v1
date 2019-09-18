import numpy as np
    
def mot_non_associated(detections=None,Y_set=None,ISO=None,st_fr=None,en_fr=None,*args,**kwargs):
    #from 0 to 5
    for i in range(0,st_fr):
        ISO.meas.append([])
    for i in range(st_fr,en_fr):
        iso_idx=np.where(Y_set[i].iso_idx == 1)
        child = []
        for j in iso_idx[0]:
            child.append(np.array(detections[i][j][:6]))
        ISO.meas.append(child)
    return ISO
    
if __name__ == '__main__':
    pass
    

