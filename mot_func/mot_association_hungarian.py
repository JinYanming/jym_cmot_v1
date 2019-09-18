import numpy as np
from Common.munkres import munkres    
def mot_association_hungarian(score_mat=None,thr=None,*args,**kwargs):

    
    if score_mat.shape[0] == 1:
        assignment,cost=munkres(- (score_mat.T))
        assignment=assignment.T
        ass_row,ass_col=np.where(assignment == 1)
    else:
        assignment,cost=munkres(- (score_mat))#matching by hungarian agriolthm
        ass_row,ass_col=np.where(assignment == 1)#choose the successfully matched part of the matrix from the score_mat and return by rows and cols
    match_cost=score_mat[assignment.astype(np.bool)]#use the assignment as a mask to get the matching part matrix score cost matrix
    midx=np.where(match_cost > thr)#select the match cost > thr element and return the index of them;The cost here means affinity socre between tracklet and detections rather than the common meaning cost,so we choose the bigger score at least bigger than thr as our qualified score
    matching=np.array([ass_row[midx],ass_col[midx]])#cause the matched part of the matrix will get a shape like nxn so the element selected by rows and cols will be a 1D list,and we choose the score bigger than thr by midx
    score=match_cost[midx]#choose the score bigger than thr by use the midx as mask
    return matching,score
    
if __name__ == '__main__':
    pass
    

