# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fPCA.m

    
@function
def fPCA(featureVectorInCol=None,eigenThreshold=None,*args,**kwargs):
    varargin = fPCA.varargin
    nargin = fPCA.nargin

    # -----------------------------------------------------------------------
# Low-dimensional batch eigen-computation when M>>N
    
    # written by T-K, Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# featureVectorInCol: MxN matrix - input data, M=dimension, N=noOfSample
# eigenThreshold: 1x1 value - the min value of eigenvalues to be selected
    
    # Output:
# principalComponents: MxR matrix - each column is a PC, R is the reduced dimension
# eigenValues: RxR - diagonal matrix storing the eigenvalues which are > eigenThreshold
# meanVector: Mx1 vector - the mean vector of the input data
# projectedData: RxN matrix - the projected data organised in column
# -----------------------------------------------------------------------
    
    noOfDimension,noOfSample=size(featureVectorInCol,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:20
    meanVector=mean(featureVectorInCol,2)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:21
    
    featureVectorInCol=double(featureVectorInCol)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:23
    data=featureVectorInCol - repmat(meanVector,1,noOfSample)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:24
    normCovMatrix=dot(data.T,data)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:26
    
    V_NN,S_NN,V_NNT=svd(normCovMatrix,nargout=3)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:27
    
    # Component selection
    testRow=diag(S_NN)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:30
    testIdx=find(testRow > eigenThreshold)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:31
    V_NN=V_NN(arange(),testIdx)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:32
    S_NN=diag(testRow(testIdx))
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:33
    invSigma_NN=inv(diag(sqrt(diag(S_NN))))
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:36
    principalComponents=dot(data,(dot(V_NN,invSigma_NN)))
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:37
    
    eigenValues=copy(S_NN)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:38
    projectedData=dot(principalComponents.T,data)
# /workspace/MOT/cmot-v1/ILDA/fPCA.m:39