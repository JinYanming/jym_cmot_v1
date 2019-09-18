import numpy as np
from kf_func.kf_loop import kf_loop
from kf_func.kf_predict import kf_predict
def km_estimation(X=None,Y=None,param=None,P=None,*args,**kwargs):

# X: object motion state, (x_pos, x_vel, y_pos, y_vel)
# Y: measurements, (x_pos, y_pos)
    checkP_isNone = lambda x: False if isinstance(x,np.ndarray) else None
    if checkP_isNone(P) == None:
        P=param.P
    
    H=param.H
    R=param.R
    Ts=param.Ts
    F1=np.array([[1,Ts],[0,1]])
    Fz=np.zeros((2,2))
    param.F = np.c_[np.r_[F1,Fz],np.r_[Fz,F1]]
    A=param.F
    Q=param.Q
    if len(Y) != 0:
        MM,PP=kf_loop(X,P,H,R,Y,A,Q)
    else:
        MM,PP=kf_predict(X,P,A,Q)
        PP=PP[:,:,np.newaxis]
    return MM,PP
    
if __name__ == '__main__':
    pass
    
