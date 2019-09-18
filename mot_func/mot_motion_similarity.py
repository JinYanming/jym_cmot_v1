import numpy as np
from Common.motion_affinity import motion_affinity
from kf_func.km_estimation import km_estimation
def mot_motion_similarity(Refer=None,Test=None,param=None,type_=None,*args,**kwargs):

    
    pos_var=param.pos_var
    if 'Obs' == type_:
        XX=Refer.FMotion.X[:,-1]
        refer_pos=[XX[0],XX[2]]
        test_pos=Test.pos
        mot_sim=motion_affinity(refer_pos,test_pos,pos_var)
    else:
        if 'Trk' == type_:
            fgap=(Test.init_time - Refer.end_time)
            if fgap > 0:
                init_time=Test.init_time
                FX=Refer.FMotion.X[:,init_time]
                BX=Test.BMotion.X[:,-1]
                BP=Test.BMotion.P[:,:,-1]
                while fgap > 0:
                    BP = BP.squeeze()
                    BX,BP=km_estimation(BX,[],param,BP,nargout=2)
                    fgap=fgap - 1

                # Forward motion
                refer_pos=[FX[1],FX[3]]
                test_pos=[Test.BMotion.X[0,-1],Test.BMotion.X[2,-1]]
                mot_sim1=motion_affinity(refer_pos,test_pos,pos_var)
                refer_pos=[BX[0],BX[2]]
                test_pos=[Refer.FMotion.X[1,-1],Refer.FMotion.X[3,-1]]
                mot_sim2=motion_affinity(refer_pos,test_pos,pos_var)
                mot_sim=np.dot(mot_sim1,mot_sim2)
            else:
                mot_sim=0
        else:
            warning('Unexpected type. Choose Obs or Trk.')
    return mot_sim
    

