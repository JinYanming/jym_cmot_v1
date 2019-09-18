import numpy as np
from mot_func.mot_is_reg import mot_is_reg
from mot_func.mot_count_ids import mot_count_ids
def MOT_Type_Update(rgbimg=None,Trk=None,param=None,cfr=None,*args,**kwargs):

    
    del_idx=[]
    lb_idx=[]
    max_frame=50
    type_thr = param.type_thr
    for i in range(0,len(Trk)):
        Conf_prob=Trk[i].Conf_prob
        type_=Trk[i].type
        if 'High' == type_:
            if Conf_prob < type_thr:
                Trk[i].type = 'Low'
                Trk[i].efr = cfr
        else:
            if 'Low' == type_:
                if Conf_prob > type_thr:
                    Trk[i].type = 'High'
                efr=Trk[i].efr
                if np.abs(cfr - efr) >= max_frame:
                    del_idx.append(i)
                    lb_idx.append(Trk[i].label)
    
    R_pos = rgbimg.shape[:2]
    L_pos=np.array([0,0])
    margin=np.array([0,0])
    for i in range(0,len(Trk)):
        tstates=Trk[i].state[-1]
        if np.isnan(tstates[0]):
            del_idx.append(i)
        else:
            fmotion=Trk[i].state[-1]
            C_pos = np.array(fmotion[0:2])
            L_pos=L_pos + margin
            R_pos=R_pos - margin

            print("**"*80)
            print(C_pos,L_pos,R_pos)
            if not mot_is_reg(C_pos,L_pos,R_pos):
                del_idx.append(i)
    
    
    del_idx = np.array(del_idx)
    if len(del_idx) != 0:
        print(del_idx)
        for idx in sorted(del_idx,reverse=True):
            mot_count_ids(Trk[idx],param)
            Trk.pop(idx)
    
    return Trk
    
if __name__ == '__main__':
    pass
    

