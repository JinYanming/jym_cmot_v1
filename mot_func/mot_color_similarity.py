import numpy as np
    
def mot_color_similarity(refer_hist=None,target_hist=None,var=None,*args,**kwargs):

    if var != None:
        N,M=size(target_hist,nargout=2)
        bhattcoeff=sum(sqrt(multiply(refer_hist,target_hist)))
        Dist=sqrt(ones(1,M) - bhattcoeff)
        likelihood=exp(sum(dot((- 1 / var),Dist ** 2)))
    else:
        likelihood=color_similarity_only_bhat(refer_hist,target_hist)
    
    return likelihood
    
    
    
def color_similarity_only_bhat(refer_hist=None,target_hist=None,*args,**kwargs):

    method=1
    bhattcoeff=np.sum(np.sqrt(refer_hist*target_hist))
    if bhattcoeff > 1:
        #r,p=corrcoef(refer_hist,target_hist,nargout=2)
        likelihood = None
        print("color error")
        #likelihood=p(1,2)
    else:
        likelihood=np.mean(bhattcoeff)
    
    return likelihood
    
if __name__ == '__main__':
    res = mot_color_similarity(np.array([1,2,3])/10,np.array([1,5,6])/10)
    print(res)
    pass
    

