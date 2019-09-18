# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fGetStModel.m

    
@function
def fGetStModel(featureVectorInCol=None,eigenThreshold=None,*args,**kwargs):
    varargin = fGetStModel.varargin
    nargin = fGetStModel.nargin

    # -----------------------------------------------------------------------
# Performing principal component analysis of total scatter matrix
    
    # written by T-K. Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# featureVectorInCol: MxN matrix - each column is a feature vector of the raw dataset, M - dimension size, N - the number of sample
# eigenThreshold: 1x1 value - the min value of eigenvalues to be selected
    
    # Output:
# meanVector: Mx1 vector - the mean vector of the raw data
# noOfSample: 1x1 value - the number of sample in the raw data
# eigenVectors: MxR matrix - each column is a principal component, R is the reduced dimension
# eigenValues: RxR matrix - diagonal matrix storing the eigenvalues of the total scatter matrix
# -----------------------------------------------------------------------
    
    noOfDimension,noOfSample=size(featureVectorInCol,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fGetStModel.m:20
    principalComponents,tmpEigVal,meanVector,reducedData=fPCA(featureVectorInCol,eigenThreshold,nargout=4)
# /workspace/MOT/cmot-v1/ILDA/fGetStModel.m:22
    eigenVectors=copy(principalComponents)
# /workspace/MOT/cmot-v1/ILDA/fGetStModel.m:24
    eigenValues=copy(tmpEigVal)
# /workspace/MOT/cmot-v1/ILDA/fGetStModel.m:25