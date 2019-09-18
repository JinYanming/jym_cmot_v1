# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m

    
@function
def fMergeSt(inMean_1=None,inNS_1=None,inEVect_1=None,inEVal_1=None,inMean_2=None,inNS_2=None,inEVect_2=None,inEVal_2=None,eigenThreshold=None,*args,**kwargs):
    varargin = fMergeSt.varargin
    nargin = fMergeSt.nargin

    # -----------------------------------------------------------------------
# Merging two "total scatter matrices"
    
    # The detailed algorithm here is the same as P.Hall and et al.'s method
# just except the covariance matrix is replaced by the scatter matrix.
# (P.Hall, D.Marshall and R.Martin, Merging and splitting eigenspace
# models, IEEE Trans. on PAMI, 2000.)
    
    # written by T-K. Kim and S-F. Wong, 2007
# -----------------------------------------------------------------------
    
    # Input:
# inMean_1: Mx1 matrix - the mean vector of the old data 
# inNS_1: 1x1 value - the number of sample in the old data
# inEVect_1: MxR_1 matrix - each column is an eigenvector of the total scatter matrix of the old data, R_1 is the reduced dimension
# inEVal_1: R_1xR_1 matrix - diagonal matrix storing the eigenvalues of the total scatter matrix of the old data
# inMean_2: Mx1 matrix - the mean vector of the new data 
# inNS_2: 1x1 value - the number of sample in the new data
# inEVect_2: MxR_2 matrix - each column is an eigenvector of the total scatter matrix of the new data, R_2 is the reduced dimension
# inEVal_2: R_2xR_2 matrix - diagonal matrix storing the eigenvalues of the total scatter matrix of the new data
    
    # Output:
# outMean: Mx1 vector - the updated mean vector of all raw data, M is the dimension
# outNSample: 1x1 value - the number of sample in the raw data
# outEVect: MxR matrix - each column is an eigenvector of the total scatter matrix, R is the reduced dimension
# outEVal: RxR matrix - diagonal matrix storing the eigenvalues of the total scatter matrix
# -----------------------------------------------------------------------
    
    # updating global mean
    outNSample=inNS_1 + inNS_2
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:31
    outMean=(dot(inMean_1,inNS_1) + dot(inMean_2,inNS_2)) / outNSample
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:32
    # QR:
    residueThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:36
    GMatrix=dot(inEVect_1.T,inEVect_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:38
    
    meanDiff=inMean_1 - inMean_2
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:39
    residue=inEVect_2 - dot(inEVect_1,(GMatrix))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:40
    
    residueSumRow=sum(abs(residue),1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:41
    pureResidue=residue(arange(),find(residueSumRow > residueThreshold))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:42
    meanResidue=meanDiff - dot(inEVect_1,(dot(inEVect_1.T,meanDiff)))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:43
    
    meanResidueSumRow=sum(abs(meanResidue),1)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:44
    meanResidue=meanResidue(arange(),find(meanResidueSumRow > residueThreshold))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:45
    OrthSubMatrix,upperTri=qr(concat([pureResidue,meanResidue]),0,nargout=2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:47
    
    # QR redundancy removal:
    qrThreshold=0.0001
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:50
    upperTriSum=sum(abs(upperTri),2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:51
    upperTriRowIndex=find(upperTriSum > qrThreshold).T
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:52
    OrthSubMatrix=OrthSubMatrix(arange(),upperTriRowIndex)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:53
    #SVD
    TMatrix=dot(OrthSubMatrix.T,inEVect_2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:56
    
    mGMatrix=dot(inEVect_1.T,meanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:57
    
    mTMatrix=dot(OrthSubMatrix.T,meanDiff)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:58
    
    reducedDim=size(inEVect_1,2) + size(OrthSubMatrix,2)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:60
    term1=zeros(reducedDim,reducedDim)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:62
    term1[arange(1,size(inEVect_1,2)),arange(1,size(inEVect_1,2))]=inEVal_1
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:63
    term2=concat([[dot(dot(GMatrix,inEVal_2),GMatrix.T),dot(dot(GMatrix,inEVal_2),TMatrix.T)],[dot(dot(TMatrix,inEVal_2),GMatrix.T),dot(dot(TMatrix,inEVal_2),TMatrix.T)]])
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:64
    
    term3=dot(concat([[dot(mGMatrix,mGMatrix.T),dot(mGMatrix,mTMatrix.T)],[dot(mTMatrix,mGMatrix.T),dot(mTMatrix,mTMatrix.T)]]),((dot(inNS_1,inNS_2)) / (outNSample)))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:65
    
    CompositeMatrix=term1 + term2 + term3
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:67
    
    U,Sigma,V_T=svd(CompositeMatrix,nargout=3)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:68
    
    testRow=diag(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:70
    testIdx=find(testRow > eigenThreshold)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:71
    U=U(arange(),testIdx)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:73
    Sigma=diag(testRow(testIdx))
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:74
    outEVal=copy(Sigma)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:76
    outEVect=dot(concat([inEVect_1,OrthSubMatrix]),U)
# /workspace/MOT/cmot-v1/ILDA/fMergeSt.m:77
    