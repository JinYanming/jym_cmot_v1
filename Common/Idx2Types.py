import numpy as np
def Idx2Types(Trk=None,type_=None,*args,**kwargs):

    
    indx=[]
    reliable=[]
    new=[]
    for i in range(0,len(Trk)):
        if Trk[i].type == type_:
            indx.append(i)
            if Trk[i].reliable == 1:
                reliable.append(i)
            if Trk[i].isnew == 1:
                new.append(i)
    
    return np.array(indx),np.array(reliable),np.array(new)
    
if __name__ == '__main__':
    pass
    
