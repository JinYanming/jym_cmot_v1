import numpy as np
    
def motion_affinity(x=None,mean=None,var=None,*args,**kwargs):
    x = np.array(x)
    mean = np.array(mean)
    
    prob_pdf=np.exp(np.dot(np.dot(np.dot(-0.5,(x - mean).T),np.linalg.inv(var)),(x - mean)))
    return prob_pdf
