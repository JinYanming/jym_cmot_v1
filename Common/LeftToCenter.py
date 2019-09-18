# Generated with SMOP  0.41
from libsmop import *
# /workspace/MOT/cmot-v1/Common/LeftToCenter.m

    
@function
def LeftToCenter(x=None,y=None,height=None,width=None,*args,**kwargs):
    varargin = LeftToCenter.varargin
    nargin = LeftToCenter.nargin

    ## Copyright (C) 2014 Seung-Hwan Bae
## All rights reserved.
    
    h_height=height / 2
# /workspace/MOT/cmot-v1/Common/LeftToCenter.m:6
    h_width=width / 2
# /workspace/MOT/cmot-v1/Common/LeftToCenter.m:7
    C_x=x + round(h_width)
# /workspace/MOT/cmot-v1/Common/LeftToCenter.m:9
    C_y=y + round(h_height)
# /workspace/MOT/cmot-v1/Common/LeftToCenter.m:10
    return C_x,C_y
    
if __name__ == '__main__':
    pass
    