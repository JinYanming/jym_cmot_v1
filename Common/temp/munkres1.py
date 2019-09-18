# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/Common/munkres.m

    while 1:

        #**************************************************************************
#   STEP 3: Cover each column with a starred zero. If all the columns are
#           covered then the matching is maximum
#**************************************************************************
        primeZ=false(n)
# /workspace/MOT/cmot-v1/Common/munkres.m:6
        coverColumn=any(starZ)
# /workspace/MOT/cmot-v1/Common/munkres.m:7
        if logical_not(any(logical_not(coverColumn))):
            break
        coverRow=false(n,1)
# /workspace/MOT/cmot-v1/Common/munkres.m:11
        # STEP 5:
    #  Construct a series of alternating primed and starred zeros as
    #  follows:
    #  Let Z0 represent the uncovered primed zero found in Step 4.
    #  Let Z1 denote the starred zero in the column of Z0 (if any).
    #  Let Z2 denote the primed zero in the row of Z1 (there will always
    #  be one).  Continue until the series terminates at a primed zero
    #  that has no starred zero in its column.  Unstar each starred
    #  zero of the series, star each primed zero of the series, erase
    #  all primes and uncover every line in the matrix.  Return to Step 3.
    #**************************************************************************
        rowZ1=starZ(arange(),uZc)
# /workspace/MOT/cmot-v1/Common/munkres.m:24
        starZ[uZr,uZc]=true
# /workspace/MOT/cmot-v1/Common/munkres.m:25
        while any(rowZ1):

            starZ[rowZ1,uZc]=false
# /workspace/MOT/cmot-v1/Common/munkres.m:27
            uZc=primeZ(rowZ1,arange())
# /workspace/MOT/cmot-v1/Common/munkres.m:28
            uZr=copy(rowZ1)
# /workspace/MOT/cmot-v1/Common/munkres.m:29
            rowZ1=starZ(arange(),uZc)
# /workspace/MOT/cmot-v1/Common/munkres.m:30
            starZ[uZr,uZc]=true
# /workspace/MOT/cmot-v1/Common/munkres.m:31


    