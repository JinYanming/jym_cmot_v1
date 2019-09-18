# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m

    
@function
def fGetSbModel_v2(featureVectorInCol=None,featureLabel=None,eigenThreshold=None,*args,**kwargs):
    varargin = fGetSbModel_v2.varargin
    nargin = fGetSbModel_v2.nargin

    # -----------------------------------------------------------------------
# Performing principal component analysis of between-class scatter matrix
    
    # written by T-K. Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# featureVectorInCol: MxN matrix - each column is a feature vector of the raw dataset, M - dimension size, N - the number of sample
# featureLabel: 1xN vector - each cell stores the class label of a sample
# eigenThreshold: 1x1 value - the min value of eigenvalues to be selected
    
    # Output:
# meanVector: Mx1 vector - the mean vector of all raw data, M is the dimension
# noOfSample: 1x1 value - the number of sample in the raw data
# eigenVectors: MxR matrix - each column is an eigenvector of the between scatter matrix, R is the reduced dimension
# eigenValues: RxR matrix - diagonal matrix storing the eigenvalues of the between scatter matrix
# samplePerClass: 1xC vector - each cell stores the number of sample per class, and C is the number of class
# meanPerClass: RxC matrix - each column stores the mean vector of a certain class
# -----------------------------------------------------------------------
    
    noOfDimension,noOfSample=size(featureVectorInCol,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:24
    labelSet=unique(featureLabel)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:26
    noOfClass=size(labelSet,2)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:27
    meanVector=mean(featureVectorInCol,2)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:29
    
    samplePerClass=zeros(1,noOfClass)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:30
    meanPerClass=zeros(noOfDimension,noOfClass)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:31
    #O(MN)
    for i in arange(1,noOfClass).reshape(-1):
        classIndex=find(featureLabel == labelSet(i))
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:35
        samplePerClass[1,i]=length(classIndex)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:36
        classMean=mean(featureVectorInCol(arange(),classIndex),2)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:37
        meanPerClass[arange(),i]=classMean
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:38
    
    meanMatrix=repmat(meanVector,1,noOfClass)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:41
    PhiMatrix=multiply((meanPerClass - meanMatrix),repmat(sqrt(samplePerClass),noOfDimension,1))
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:42
    
    S_b=dot(PhiMatrix.T,PhiMatrix)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:43
    
    U,Sigma,V_T=svd(S_b,nargout=3)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:45
    
    testRow=diag(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:47
    testIdx=find(testRow > eigenThreshold)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:48
    
    U=U(arange(),testIdx)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:49
    Sigma=diag(testRow(testIdx))
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:50
    eigenVectors=dot(PhiMatrix,(dot(U,inv(sqrt(Sigma)))))
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:52
    
    eigenValues=copy(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:53
    meanPerClass=dot(eigenVectors.T,(meanPerClass - repmat(meanVector,1,size(meanPerClass,2))))
# /workspace/MOT/cmot-v1/ILDA/fGetSbModel_v2.m:55