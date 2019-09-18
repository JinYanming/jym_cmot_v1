# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/Common/CenterToLeft.m

    
@function
def CenterToLeft(x=None,y=None,height=None,width=None,*args,**kwargs):
    varargin = CenterToLeft.varargin
    nargin = CenterToLeft.nargin

    ## Copyright (C) 2014 Seung-Hwan Bae
## All rights reserved.
    
    # (x,y): Center position
    
    h_height=height / 2
# /workspace/MOT/cmot-v1/Common/CenterToLeft.m:7
    h_width=width / 2
# /workspace/MOT/cmot-v1/Common/CenterToLeft.m:8
    L_x=x - round(h_width)
# /workspace/MOT/cmot-v1/Common/CenterToLeft.m:10
    L_y=y - round(h_height)
# /workspace/MOT/cmot-v1/Common/CenterToLeft.m:11
    return L_x,L_y
    
if __name__ == '__main__':
    pass
    