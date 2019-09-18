import numpy as np
import math
def affparam2mat(p = None,*args,**kwargs):

# function q  =  affparam2mat(p)
    
# The functions affparam2geom and affparam2mat convert a 'geometric'
# affine parameter to/from a matrix form (2x3 matrix).
# 
# affparam2geom converts a 2x3 matrix to 6 affine parameters
# (x, y, th, scale, aspect, skew), and affparam2mat does the inverse.
#    p(6,n) : [dx dy sc th sr phi]'
#    q(6,n) : [q(1) q(3) q(4); q(2) q(5) q(6)]

# Reference "Multiple View Geometry in Computer Vision" by Richard
# Hartley and Andrew Zisserman.


    sz = [len(p[0]),len(p)]
    #if (sz[1]  ==  6):
    #   p = p
    p = np.array(p)
    p = np.swapaxes(p,0,1)
    s = p[2,:]
    th = p[3,:]
    r = p[4,:]
    phi = p[5,:]
    cth = np.cos(th).astype(np.float32)
    sth = np.sin(th).astype(np.float32)
    cph = np.cos(phi).astype(np.float32)
    sph = np.sin(phi).astype(np.float32)
    np_array = True if sz[1] > 1 else False
    ccc=cth*cph*cph
    ccs=cth*cph*sph
    css=cth*sph*sph
    scc=sth*cph*cph
    scs=sth*cph*sph
    sss=sth*sph*sph
    
    q = np.zeros((sz[0],sz[1]))
    q[0,:] = p[0,:]
    q[1,:] = p[1,:]
    q[2,:] = s*(ccc + scs + r*(css - scs))
    q[3,:] = s*(r*(ccs - scc) - ccs - sss)
    q[4,:] = s*(scc - ccs + r*(ccs + sss))
    q[5,:] = s*(r*(ccc + scs) - scs + css)
    q = np.reshape(q,sz)
    q = np.swapaxes(q,0,1)
    return q
