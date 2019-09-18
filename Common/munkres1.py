import numpy as np
from Common.magic import magic
def munkres(costMat = None,*args,**kwargs):

# MUNKRES   Munkres Assign Algorithm
    
# [ASSIGN,COST]  =  munkres(COSTMAT) returns the optimal assignment in ASSIGN
# with the minimum COST based on the assignment problem represented by the
# COSTMAT, where the (i,j)th element represents the cost to assign the jth
# job to the ith worker.
    
# This is vectorized implementation of the algorithm. It is the fastest
# among all Matlab implementations of the algorithm.
    
# Examples
# Example 1: a 5 x 5 example
#{
#    assignment,cost = munkres(magic(5),nargout = 2)
#    assignedrows,dum = find(assignment,nargout = 2)
#    print(assignedrows.T)    
#    print(cost)
#}
# Example 2: 400 x 400 random data
#{
#    n = 400
#    A = rand(n)
#    tic
#    a,b = munkres(A,nargout = 2)
#    toc
#    }    
#     Reference:
# "Munkres' Assignment Algorithm, Modified for Rectangular Matrices", 
# http://csclab.murraystate.edu/bob.pilgrim/445/munkres.html   
# version 1.0 by Yi Cao at Cranfield University on 17th June 2008
    assignment = np.zeros(costMat.shape)
    cost = 0
    costMat[costMat !=  costMat] = np.Inf
    validMat = (costMat < np.Inf) + 0
    validCol = np.any(validMat,0) + 0
    validRow = np.any(validMat,1) + 0
    nRows = np.sum(validRow)
    nCols = np.sum(validCol)
    n = max(nRows,nCols)
    if not n:
        return assignment,cost
    
    
    dMat = np.zeros((n,n))
    dMat[:nRows,:nCols] = costMat*np.dot(validRow[:,np.newaxis],validCol[np.newaxis,:])
#*************************************************
# Munkres' Assignment Algorithm starts here
#*************************************************
    
#########################################################
#   STEP 1: Subtract the row minimum from each row.
#########################################################
    print("**********")
    print(dMat)
    print(np.min(dMat,1))
    dMat = dMat-(np.min(dMat,1)[:,np.newaxis]) 
    print(dMat)
#**************************************************************************  
#   STEP 2: Find a zero of dMat. If there are no starred zeros in its
#           column or row start the zero. Repeat for each zero
#**************************************************************************
    zP = ~dMat.astype(np.bool)+0
    starZ = np.zeros((n,n))
    while np.any(np.ravel(zP)):

        r,c = np.where(zP!=0)
        r = r[0]
        c = c[0]
        starZ[r,c] = True
        zP[r,:] = False
        zP[:,c] = False

    while 1:

#**************************************************************************
#   STEP 3: Cover each column with a starred zero. If all the columns are
#           covered then the matching is maximum
#**************************************************************************
        primeZ = np.zeros((n,n))
        coverColumn = np.any(starZ,0)[np.newaxis,:]
        if not np.any(~coverColumn):
            break
        coverRow = np.zeros((n,1))
        while 1:

                     #**************************************************************************
        #   STEP 4: Find a noncovered zero and prime it.  If there is no starred
        #           zero in the row containing this primed zero, Go to Step 5.  
        #           Otherwise, cover this row and uncover the column containing 
        #           the starred zero. Continue in this manner until there are no 
        #           uncovered zeros left. Save the smallest uncovered value and 
        #           Go to Step 6.
        #**************************************************************************
            coverRow = coverRow.astype(np.bool)
            coverColumn = coverColumn.astype(np.bool)
            zP = np.full(zP.shape,False)
            mask = ~coverRow*~coverColumn
            print("mask",mask)
            print("zP:",zP)
            print("~dMat",~dMat.astype(np.bool)+0)
            zP = (zP*~mask+0)+(~dMat.astype(np.bool)*(mask)+0)
            zP = zP.astype(np.bool)
            print("zP:",zP)
            Step = 6
            while np.any(np.any(zP*mask,0),0):

                uZr,uZc = find(zP,1,nargout = 2)
                primeZ[uZr,uZc] = true
                stz = starZ(uZr,arange())
                if logical_not(any(stz)):
                    Step = 5
                    break
                coverRow[uZr] = True
                coverColumn[stz] = False
                zP[uZr,arange()] = False
                zP[logical_not(coverRow),stz] = logical_not(dMat(logical_not(coverRow),stz))

            if Step  ==  6:
                # *************************************************************************
            # STEP 6: Add the minimum uncovered value to every element of each covered
            #         row, and subtract it from every element of each uncovered column.
            #         Return to Step 4 without altering any stars, primes, or covered lines.
            #**************************************************************************
                M=dMat*mask
                minval = np.min(M)
                if minval  ==  np.inf:
                    return assignment,cost
                positiveMask = coverRow*coverColumn
                dMat[coverRow,coverColumn] = dMat[coverRow,coverColumn] + minval
                dMat[logical_not(coverRow),logical_not(coverColumn)] = M - minval
            else:
                break

        #**************************************************************************
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
        rowZ1 = starZ(arange(),uZc)
        starZ[uZr,uZc] = true
        while any(rowZ1):

            starZ[rowZ1,uZc] = false
            uZc = primeZ(rowZ1,arange())
            uZr = copy(rowZ1)
            rowZ1 = starZ(arange(),uZc)
            starZ[uZr,uZc] = true


    
    # Cost of assignment
    r,c = assignment.shape
    bool_index2num_index = lambda bool_index:np.array([i for i in range(0,len(bool_index))])[bool_index.astype(np.bool)]
    r = bool_index2num_index(validRow)
    c = bool_index2num_index(validCol)
    for i in r:
        for j in c:
            ii = np.where(r==i)
            jj = np.where(c==j)
            assignment[i,j] = starZ[ii,jj]
    cost = np.sum(costMat*assignment)
    return assignment,cost
