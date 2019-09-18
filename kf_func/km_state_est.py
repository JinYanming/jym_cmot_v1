import numpy as np

from kf_func.kf_loop import kf_loop
from kf_func.kf_predict import kf_predict

def km_state_est(X=None,Y=None,param=None,P=None,*args,**kwargs):
## Copyright (C) 2014 Seung-Hwan Bae
## All rights reserved.
    
# X: object motion state, (x_pos, x_vel, y_pos, y_vel)
# Y: measurements, (x_pos, y_pos)
    if P == None:
        P=param.P
    
    H=param.H
    R=param.R
    A=param.F
    Q=param.Q
    if ~np.all(Y==0):
        MM,PP=kf_loop(X,P,H,R,Y,A,Q,nargout=2)
    else:
        MM,PP=kf_predict(X,P,A,Q,nargout=2)
    
    return MM,PP
