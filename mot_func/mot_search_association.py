import numpy as np

def mot_search_association(Y=None,fr=None,prt_idx=None,*args,**kwargs):
    """
    input:
            Y,fr,prt_idx
            Y:graph
            fr:the last init frame
            prt_idx:every child dectection list from the privious frame
    output:
        ass_idx
        ass_idx:the tracklet of this object
    """
    flg = 1
    ct= 0
    ass_idx=[]
    check_none = lambda x: True if len(x) >= 1 and x[0]!=-1 else False
    if check_none(prt_idx):
        while flg == 1:
            ct=ct + 1
            getMapped = lambda c_list,p_list:[j for i in c_list for j in p_list[i]]
            prt_idx = getMapped(prt_idx,Y[fr-ct].child)
            if len(prt_idx) == 1:
                ass_idx.append(prt_idx)
                if prt_idx[0] == -1:#when it comes to -1 means the tracklet suspend
                    flg = 0
            else:
                ass_idx.append([-1])
                flg=0
            #else:
            #    ass_idx.append(prt_idx)
            #   flg=0

    
    ass_idx.reverse()
    return ass_idx
    
if __name__ == '__main__':
    pass
    

