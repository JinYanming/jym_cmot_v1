# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m

    
@function
def fGetDiscriminativeComponents_v2(totalEigVect=None,totalEigVal=None,betweenEigVect=None,betweenEigVal=None,outNSample=None,eigenThreshold=None,totalTermFactorZ_Limit=None,*args,**kwargs):
    varargin = fGetDiscriminativeComponents_v2.varargin
    nargin = fGetDiscriminativeComponents_v2.nargin

    # -----------------------------------------------------------------------
# Getting discriminative component
    
    # written by T-K. Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# totalEigVect: MxR_t matrix - each column is an eigenvector of the total scatter matrix, R_t is the reduced dimension
# totalEigVal: R_txR_t matrix - diagonal matrix storing the eigenvalues of the total scatter matrix
# betweenEigVect: MxR_b matrix - each column is an eigenvector of the between scatter matrix, R_b is the reduced dimension
# betweenEigVal: R_bxR_b matrix - diagonal matrix storing the eigenvalues of the between scatter matrix
    
    # Output:
# DiscriminativeComponents: MxR_d matrix - each column is a discriminative component, R_d is the reduced dimension
    
    
    # *Caution* : 
# LDA accuracy is dependent on the dimensionality of both
# intermediate components (total scatter matrix) and the final discriminant
# components. They should be set by a priori.
    
    # -----------------------------------------------------------------------
    
    totalTermFactorZ=dot(totalEigVect,inv(sqrt(totalEigVal)))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:26
    
    
    # here, the dimension of total scatter matrix may be controlled...
# totalTermFactorZ = totalTermFactorZ(:,1:??);
    
    num_total=floor(size(totalTermFactorZ,2))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:31
    totalTermFactorZ=totalTermFactorZ(arange(),arange(1,num_total))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:33
    # totalTermFactorZ_Limit = ILDA.totalTermFactorZ_Limit;
    if num_total > totalTermFactorZ_Limit:
        totalTermFactorZ=totalTermFactorZ(arange(),arange(1,totalTermFactorZ_Limit))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:37
    
    spanningSetTau,upperTriMat=qr(dot(totalTermFactorZ.T,betweenEigVect),0,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:40
    
    
    # removing non-significant components for further speed-up
    qrThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:43
    upperTriSum=sum(abs(upperTriMat),2)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:44
    upperTriRowIndex=find(upperTriSum > qrThreshold).T
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:45
    spanningSetTau=spanningSetTau(arange(),upperTriRowIndex)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:46
    halfMatrix=dot(spanningSetTau.T,(dot(totalTermFactorZ.T,betweenEigVect)))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:48
    
    compositeMatrix=dot(dot(halfMatrix,betweenEigVal),halfMatrix.T)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:49
    
    U_N,S_N,U_NT=svd(compositeMatrix,nargout=3)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:50
    
    testRow=diag(S_N)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:52
    testIdx=find(testRow > eigenThreshold)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:53
    U_N=U_N(arange(),testIdx)
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:54
    S_N=diag(testRow(testIdx))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:55
    DiscriminativeComponents=dot(totalTermFactorZ,(dot(spanningSetTau,U_N)))
# /workspace/MOT/cmot-v1/ILDA/fGetDiscriminativeComponents_v2.m:57
    
    # here, the dimension of the discriminant components may be controlled...