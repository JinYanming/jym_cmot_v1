import numpy as np
from Common.calc_overlap2 import calc_overlap2
from Obj.ISO import Node
def mot_pre_association_tracking(ISO=None,start_frame=None,end_frame=None,*args,**kwargs):

    #ISO.node : [[child][child]]
    for i in range(0,end_frame):
        ISO.node.append(Node()) 
    init_det=ISO.meas[start_frame]
    #ISO.node[start_frame]:[[0],[0],[0]]
    for i in range(0,len(init_det)):
        ISO.node[start_frame].child.append([-1])
    if len(init_det) != 0:
        detections=ISO.meas.copy()
        for q in range(start_frame + 1,end_frame):
            if len(detections[q-1]) != 0:
                prev_det=np.array(detections[q - 1])[:,2:]
            else:
                prev_det=np.array(detections[q - 1])
            if len(detections[q]) != 0:
                cur_det=np.array(detections[q])[:,2:]
            else:
                cur_det=np.array(detections[q])
            #for i in range(0,len(cur_det)):
            #    ISO.node[q].child.append([-1])
            asso_idx=[]
            for i in range(0,len(cur_det)):
                ovs1,_,_=calc_overlap2(cur_det,prev_det,i)
                inds1 = np.nonzero(ovs1 > 0.4)[0]#return the index of  prvious detections whose IOU with current Detection
                if len(inds1) != 0:
                    max_ovs1_location = np.where(ovs1 == np.max(ovs1))[0][0]
                    #choose the detections from the privious frame whose IOU is max and <0.4
                    inds1 = np.array([max_ovs1_location])
                    #calculate the ratio in Demesion H betweend current detection and privious detectionsf (max_ovs1_location in inds1) else inds1
                    ratio1=cur_det[i,3] / prev_det[inds1,3]
                    #select ratio1 > 0.8
                    inds2=(np.minimum(ratio1,1.0 / ratio1) > 0.8)
                    #if ratios > 0.8 exits then add these
                    if len(inds1[inds2]) > 0:
                        ISO.node[q].child.append(inds1[inds2].tolist())
                    else:
                        ISO.node[q].child.append([-1])
                    asso_idx = np.concatenate((asso_idx,inds1[inds2]),axis=0)
                else:
                    ISO.node[q].child.append([-1])
    return ISO
    
if __name__ == '__main__':
    pass
    

