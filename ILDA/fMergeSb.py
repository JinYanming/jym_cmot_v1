# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m

    
@function
def fMergeSb(inMean_1=None,inNS_1=None,inEVect_1=None,inEVal_1=None,samplePerClass_1=None,meanPerClass_1=None,featureLabel_1=None,inMean_2=None,inNS_2=None,inEVect_2=None,inEVal_2=None,samplePerClass_2=None,meanPerClass_2=None,featureLabel_2=None,eigenThreshold=None,*args,**kwargs):
    varargin = fMergeSb.varargin
    nargin = fMergeSb.nargin

    # -----------------------------------------------------------------------
# Merging two "between scatter matrices"
    
    # written by T-K. Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# inMean_1: Mx1 vector - the mean vector of the old data 
# inNS_1: 1x1 value - the number of sample in the old data
# inEVect_1: MxR_1 matrix - each column is an eigenvector of the between scatter matrix of the old data, R_1 is the reduced dimension
# inEVal_1: R_1xR_1 matrix - diagonal matrix storing the eigenvalues of the between scatter matrix of the old data
# samplePerClass_1: 1xC_1 vector - each cell stores the number of sample per class in the old data, and C_1 is the number of class
# meanPerClass_1: R_1xC_1 matrix - each column stores the mean vector of a certain class in the old data
# featureLabel_1: 1xN_1 vector - each cell stores the class label of a sample in the old data
    
    # inMean_2: Mx1 vector - the mean vector of the new data 
# inNS_2: 1x1 value - the number of sample in the new data
# inEVect_2: MxR_2 matrix - each column is an eigenvector of the total scatter matrix of the new data, R_2 is the reduced dimension
# inEVal_2: R_2xR_2 matrix - diagonal matrix storing the eigenvalues of the total scatter matrix of the new data
# samplePerClass_2: 1xC_2 vector - each cell stores the number of sample per class in the new data, and C_2 is the number of class
# meanPerClass_2: R_2xC_2 matrix - each column stores the mean vector of a certain class in the new data
# featureLabel_2: 1xN_2 vector - each cell stores the class label of a sample in the new data
    
    # Output:
# meanVector: Mx1 vector - the updated mean vector of all raw data, M is the dimension
# noOfSample: 1x1 value - the number of sample in the raw data
# eigenVectors: MxR matrix - each column is an eigenvector of the between scatter matrix, R is the reduced dimension
# eigenValues: RxR matrix - diagonal matrix storing the eigenvalues of the between scatter matrix
# samplePerClass: 1xC vector - each cell stores the number of sample per class, and C is the number of class
# meanPerClass: RxC matrix - each column stores the mean vector of a certain class
# -----------------------------------------------------------------------
    
    noOfDimension=size(inEVect_1,1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:35
    noOfSample=inNS_1 + inNS_2
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:36
    meanVector=(dot(inMean_1,inNS_1) + dot(inMean_2,inNS_2)) / (noOfSample)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:37
    # QR:
    residueThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:40
    GMatrix=dot(inEVect_1.T,inEVect_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:42
    
    meanDiff=inMean_1 - inMean_2
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:43
    residue=inEVect_2 - dot(inEVect_1,(GMatrix))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:44
    
    residueSumRow=sum(abs(residue),1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:45
    pureResidue=residue(arange(),find(residueSumRow > residueThreshold))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:46
    meanResidue=meanDiff - dot(inEVect_1,(dot(inEVect_1.T,meanDiff)))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:47
    
    meanResidueSumRow=sum(abs(meanResidue),1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:48
    meanResidue=meanResidue(arange(),find(meanResidueSumRow > residueThreshold))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:49
    OrthSubMatrix,upperTri=qr(concat([pureResidue,meanResidue]),0,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:51
    
    qrThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:53
    upperTriSum=sum(abs(upperTri),2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:54
    upperTriRowIndex=find(upperTriSum > qrThreshold).T
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:55
    OrthSubMatrix=OrthSubMatrix(arange(),upperTriRowIndex)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:56
    # ### Removing zero-columns in OrthMatrix:::
    nonZeroThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:59
    OrthMatrixSum=sum(abs(OrthSubMatrix),1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:60
    nonZeroIndex=find(OrthMatrixSum > nonZeroThreshold)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:61
    OrthSubMatrix=OrthSubMatrix(arange(),nonZeroIndex)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:62
    #SVD
    TMatrix=dot(OrthSubMatrix.T,inEVect_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:65
    
    mGMatrix=dot(inEVect_1.T,meanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:66
    
    mTMatrix=dot(OrthSubMatrix.T,meanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:67
    
    reducedDim=size(inEVect_1,2) + size(OrthSubMatrix,2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:69
    term1=zeros(reducedDim,reducedDim)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:71
    term1[arange(1,size(inEVect_1,2)),arange(1,size(inEVect_1,2))]=inEVal_1
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:72
    term2=concat([[dot(dot(GMatrix,inEVal_2),GMatrix.T),dot(dot(GMatrix,inEVal_2),TMatrix.T)],[dot(dot(TMatrix,inEVal_2),GMatrix.T),dot(dot(TMatrix,inEVal_2),TMatrix.T)]])
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:73
    
    term4=dot(concat([[dot(mGMatrix,mGMatrix.T),dot(mGMatrix,mTMatrix.T)],[dot(mTMatrix,mGMatrix.T),dot(mTMatrix,mTMatrix.T)]]),((dot(inNS_1,inNS_2)) / (noOfSample)))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:74
    
    # for common classes
    term3=zeros(reducedDim,reducedDim)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:77
    # O(C^2 M R_i)
    labelSet1=union([],featureLabel_1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:79
    labelSet2=union([],featureLabel_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:80
    labelSet_com=intersect(labelSet1,labelSet2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:81
    if (length(labelSet_com)):
        for i in arange(1,length(labelSet_com)).reshape(-1):
            idx1=find(labelSet_com(i) == labelSet1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:84
            idx2=find(labelSet_com(i) == labelSet2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:85
            coeff=(dot(- samplePerClass_1(1,idx1),samplePerClass_2(1,idx2))) / (samplePerClass_1(1,idx1) + samplePerClass_2(1,idx2))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:87
            classmeanDiff=(dot(inEVect_1,meanPerClass_1(arange(),idx1)) + inMean_1 - dot(inEVect_2,meanPerClass_2(arange(),idx2)) - inMean_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:88
            cGMatrix=dot(inEVect_1.T,classmeanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:89
            cTMatrix=dot(OrthSubMatrix.T,classmeanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:90
            term3=term3 + dot(concat([[dot(cGMatrix,cGMatrix.T),dot(cGMatrix,cTMatrix.T)],[dot(cTMatrix,cGMatrix.T),dot(cTMatrix,cTMatrix.T)]]),coeff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:91
    
    
    CompositeMatrix=term1 + term2 + term3 + term4
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:95
    
    U,Sigma,V_T=svd(CompositeMatrix,nargout=3)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:97
    
    testRow=diag(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:99
    testIdx=find(testRow > eigenThreshold)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:102
    
    U=U(arange(),testIdx)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:103
    Sigma=diag(testRow(testIdx))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:104
    eigenVectors=dot(concat([inEVect_1,OrthSubMatrix]),U)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:107
    
    eigenValues=copy(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:108
    # updates other params.
    featureLabel=horzcat(featureLabel_1,featureLabel_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:112
    labelSet=union([],featureLabel)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:113
    noOfClass=size(labelSet,2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:114
    samplePerClass=zeros(1,noOfClass)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:115
    meanPerClass=zeros(size(eigenVectors,2),noOfClass)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:116
    for i in arange(1,length(labelSet)).reshape(-1):
        idx1=find(labelSet(i) == labelSet1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:119
        idx2=find(labelSet(i) == labelSet2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:120
        subMean_3=zeros(noOfDimension,1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:121
        if (length(idx1)):
            samplePerClass[1,i]=samplePerClass(1,i) + samplePerClass_1(1,idx1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:124
            subMean_3=subMean_3 + dot(samplePerClass_1(1,idx1),(dot(inEVect_1,meanPerClass_1(arange(),idx1)) + inMean_1))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:125
        if (length(idx2)):
            samplePerClass[1,i]=samplePerClass(1,i) + samplePerClass_2(1,idx2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:128
            subMean_3=subMean_3 + dot(samplePerClass_2(1,idx2),(dot(inEVect_2,meanPerClass_2(arange(),idx2)) + inMean_2))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:129
        subMean_3=subMean_3 / samplePerClass(1,i)
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:132
        meanPerClass[arange(),i]=dot(eigenVectors.T,(subMean_3 - meanVector))
# /workspace/MOT/cmot-v1/ILDA/fMergeSb.m:133
    