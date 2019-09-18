import numpy as np
def lists2array(lists,c = None):
    """
    lists:a list which consist of list
    c:length of sublist
    """
    lists_array = np.zeros((c,0))
    for list in lists:
        if len(list) != 0:
            lists_array = np.c_[lists_array,np.array(list)[:,np.newaxis]]
    return lists_array
            
