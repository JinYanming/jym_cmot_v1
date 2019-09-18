import numpy as np
def calc_overlap2(cur_det=None,prev_det=None,i=None,*args,**kwargs):

    ##f2 can be an array and f1 should be a scalar.
### this will find the overlap between dres1(f1) (only one) and all detection windows in dres2(f2(:))
    
    ## Calculate overlap
    n2=len(prev_det)
    #curent dection x,y,h,w
    cx1=cur_det[i][0]
    cx2=cur_det[i][0] + cur_det[i][2] - 1
    cy1=cur_det[i][1]
    cy2=cur_det[i][1] + cur_det[i][3] - 1
    x = []
    y = []
    w = []
    h = []
    for temp_det in prev_det:
        x.append(temp_det[0])
        y.append(temp_det[1])
        w.append(temp_det[2])
        h.append(temp_det[3])
    #previous detections x,y,w,h
    gx1= np.array(x)
    gx2= np.array(x) + np.array(w) - 1
    gy1= np.array(y)
    gy2= np.array(y) + np.array(h) - 1
    ca=np.multiply(cur_det[i][2],(cur_det[i][3]))#the area of the current detection
    ga=np.multiply(w,h)#the areas of the previous detections
    xx1=np.maximum(cx1,gx1)#get
    yy1=np.maximum(cy1,gy1)
    xx2=np.minimum(cx2,gx2)
    yy2=np.minimum(cy2,gy2)
    w=xx2 - xx1 + 1
    h=yy2 - yy1 + 1
    inds=np.nonzero(np.multiply((w > -1),(h > 0)))
    inds = inds[0]
    ov=np.zeros((n2))
    ov_n1=np.zeros((n2))
    ov_n2=np.zeros((n2))
    inter=np.multiply(w[inds],h[inds])
    
    u=ca + ga[inds] - np.multiply(w[inds],h[inds])
    ov[inds]=inter / u  #IOU
    ov_n1[inds]=inter / ca #overlap /current area
    ov_n2[inds]=inter / ga[inds] #overlap/previous detec
    return ov,ov_n1,ov_n2
    
if __name__ == '__main__':
    pass
    
