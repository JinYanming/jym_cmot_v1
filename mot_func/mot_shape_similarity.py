import numpy as np
def mot_shape_similarity(rh=None,rw=None,th=None,tw=None,*args,**kwargs):

    Affinity=np.exp(np.dot(- 1.5,((np.abs(rh - th) / (rh + th)) + (np.abs(rw - tw) / (rw + tw)))))
    return Affinity
