import numpy as np
from Common.list2array import lists2array
def MOT_Confidence_Update(Trk=None,param=None,fr=None,lambda_=None,*args,**kwargs):

    
    if lambda_ == None:
        lambda_=1.2
    
    ## Tracklet confidence update
    
    for i in range(0,len(Trk)):
        if Trk[i].last_update == fr:
            hyp_score= np.array((Trk[i].hyp.score))
            L_T=0
            ass_idx=[]
            hyp_score_length = len(hyp_score)
            for ii in range(0,len(hyp_score)):
                ii = hyp_score_length - ii -1#reverse the range list
                if hyp_score[ii] == 0:
                    break
                L_T=L_T + 1
                ass_idx.append(ii)
            ass_idx = np.array(ass_idx).astype(np.int)
            L_T_backwards = lambda x:1/x if x !=0 else np.Inf
            Conf_prob=np.dot(np.dot(L_T_backwards(L_T),np.sum(hyp_score[ass_idx])),(1 - np.exp(np.dot(- lambda_,np.sqrt(L_T)))))
            Trk[i].Conf_prob = Conf_prob
            Trk[i].Cont_Asso = L_T
        else:
            Conf_prob=Trk[i].Conf_prob
            Trk[i].Conf_prob = np.dot(Conf_prob,param.atten)
    
    return Trk
    
if __name__ == '__main__':
    pass
    

