
#KF_PREDICT  Perform Kalman Filter prediction step
    
# Syntax:
#   [X,P] = KF_PREDICT(X,P,A,Q,B,U)
    
    # In:
#   X - Nx1 mean state estimate of previous step
#   P - NxN state covariance of previous step
#   A - Transition matrix of discrete model (optional, default identity)
#   Q - Process noise of discrete model     (optional, default zero)
#   B - Input effect matrix                 (optional, default identity)
#   U - Constant input                      (optional, default empty)
    
    # Out:
#   X - Predicted state mean
#   P - Predicted state covariance
#   
# Description:
#   Perform Kalman Filter prediction step. The model is
    
    #     x[k] = A*x[k-1] + B*u[k-1] + q,  q ~ N(0,Q).
# 
#   The predicted state is distributed as follows:
#   
#     p(x[k] | x[k-1]) = N(x[k] | A*x[k-1] + B*u[k-1], Q[k-1])
    
    #   The predicted mean x-[k] and covariance P-[k] are calculated
#   with the following equations:
    
    #     m-[k] = A*x[k-1] + B*u[k-1]
#     P-[k] = A*P[k-1]*A' + Q.
    
    #   If there is no input u present then the first equation reduces to
#     m-[k] = A*x[k-1]
    
    # History:
    
    #   26.2.2007 JH Added the distribution model for the predicted state
#                and equations for calculating the predicted state mean and
#                covariance to the description section.
#  
# See also:
#   KF_UPDATE, LTI_DISC, EKF_PREDICT, EKF_UPDATE
    
    # Copyright (C) 2002-2006 Simo S?kk?
# Copyright (C) 2007 Jouni Hartikainen
    
    # $Id: kf_predict.m 111 2007-09-04 12:09:23Z ssarkka $
    
    # This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.
import numpy as np    
    
def kf_predict(x=None,P=None,A=None,Q=None,B=None,u=None,*args,**kwargs):
    nargin = kf_predict.__code__.co_varnames
    nargin = len(nargin)
    # Check arguments
    
    if nargin < 6:
        A=np.array([])
    
    if nargin < 7:
        Q=np.array([])
    
    if nargin < 8:
        B=np.array([])
    
    if nargin < 9:
        u=np.array([])
    
    
    
    # Apply defaults
    
    if np.all(A==0):
        A=eye(size(x,1))
    
    if np.all(Q==0):
        Q=zeros(size(x,1))
    
    if np.all(B==0) and ~np.all(u==0):
        B=eye(size(x,1),size(u,1))
    
    # Perform prediction
    if u == None:
        x= np.matmul(A,x)
        temp = np.matmul(A,P)
        temp = np.matmul(temp,A.T)
        temp = temp + Q
        P=np.matmul(np.matmul(A,P),A.T) + Q
    else:
        x=np.matmul(A,x) + np.matmul(B,u)
        P=np.matmul(np.matmul(A,P),A.T) + Q
        P = P[:,:,np.newaxis]
    return x,P
    
