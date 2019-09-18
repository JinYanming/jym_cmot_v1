import numpy as np
    
def mot_return_ass_idx(child_idx=None,prt_idx=None,root_idx=None,c_fr=None,*args,**kwargs):
    """
    intput:
            child_idx:init Tracklet
            prt_idx :child i in the last frame of init frames in grap
            root_idx:index i.means the index mapped by child
            c_fr:the last frame of the init frame

    return:
        all_idx:
    content:
        all_idx:the
    """

    all_idx = [[-1]]*(c_fr+1)#shape [1,5]
    all_idx[-1] = [root_idx]
    all_idx[-2] = prt_idx
    nofc = len(child_idx)
    all_idx[-1-nofc:-1-1] = child_idx[1:]
    return all_idx
    
if __name__ == '__main__':
    pass
    

