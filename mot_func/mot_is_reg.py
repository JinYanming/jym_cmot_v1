import numpy as np
    
def mot_is_reg(pos=None,left=None,right=None,*args,**kwargs):

    
    Lx=left[0]
    Ly=left[1]
    Rx=right[1]
    Ry=right[0]
    if (pos[0] > Lx and pos[0] < Rx) and (pos[1] > Ly and pos[1] < Ry):
        decision = 1
    else:
        decision = 0
    
    return decision
    

