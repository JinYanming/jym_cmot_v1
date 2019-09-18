
#KF_LOOP  Performs the prediction and update steps of the Kalman filter
#         for a set of measurements.
    
# Syntax:
#   [MM,PP] = KF_LOOP(X,P,H,R,Y,A,Q)
# 
# In:
#   X - Nx1 initial estimate for the state mean 
#   P - NxN initial estimate for the state covariance
#   H - DxN measurement matrix
#   R - DxD measurement noise covariance
#   Y - DxM matrix containing all the measurements.
#   A - Transition matrix of the discrete model (optional, default identity)
#   Q - Process noise of the discrete model     (optional, default zero)
#   
# Out:
#   MM - Filtered state mean sequence
#   PP - Filtered state covariance sequence
#  
#  Description:
#    Calculates state estimates for a set measurements using the
#    Kalman filter. This function is for convience, as it basically consists
#    only of a space reservation for the estimates and of a for-loop which
#    calls the predict and update steps of the KF for each time step in
#    the measurements.  
#  
#  See also:
#    KF_PREDICT, KF_UPDATE
    
    #  History:
#   
#    12.2.2007 JH Initial version.
    
    # Copyright (C) 2007 Jouni Hartikainen
    
    # This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.
    
import numpy as np
from kf_func.kf_predict import kf_predict
from kf_func.kf_update import kf_update
def kf_loop(X=None,P=None,H=None,R=None,Y=None,A=None,Q=None,*args,**kwargs):
    nargin = kf_loop.__code__.co_varnames
    nargin = len(nargin)#get the number of parameters
    if not isinstance(Y,np.ndarray):
        Y = np.array(Y)
    # Check the input parameters.
    if nargin < 5:
        error('Too few arguments')
    
    if nargin < 6:
        A=[]
    
    if nargin < 7:
        Q=[]
    
    # Apply the defaults
    if np.all(A==0):
        A = np.eye(X.shape[0])
    
    if np.all(Q==0):
        Q = np.zeros(X.shape)
    
    # Space for the estimates.
    if len(Y.shape) < 2:
        Y = Y[:,np.newaxis]
    if len(X.shape) < 2:
        X = X[:,np.newaxis]
    try:
        MM = np.zeros((X.shape[0],Y.shape[1]))
        PP = np.zeros((X.shape[0],X.shape[0],Y.shape[1]))
    except Exception:
        print("dims of Y is less than 2!")
    for i in range(0,Y.shape[1]):
        X,P=kf_predict(X,P,A,Q,nargout=2)
        X,P,_,_,_,_=kf_update(X,P,Y[:,i],H,R,nargout=2)
        MM[:,i]=X.squeeze()
        PP[:,:,i]=P
    
    return MM,PP
    
