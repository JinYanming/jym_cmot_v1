import numpy as np
from kf_func.km_state_update import km_state_update
def MOT_State_Update(Trk=None,param=None,fr=None,*args,**kwargs):

    for i in range(0,len(Trk)):
        if Trk[i].last_update == fr:
            new_tmpl=Trk[i].hyp.new_tmpl
            old_tmpl=Trk[i].A_Model
            alpha=0.1
            Trk[i].A_Model = np.dot((1 - alpha),old_tmpl) + np.dot(alpha,new_tmpl)
            ystate=Trk[i].hyp.ystate[fr]
            Trk[i]=km_state_update(Trk[i],ystate,param,fr)
        else:
            Trk[i]=km_state_update(Trk[i],[],param,fr)
    
    return Trk
    
if __name__ == '__main__':
    pass
    

