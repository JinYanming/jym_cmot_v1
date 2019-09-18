import numpy as np
import scipy.ndimage
import math
import cv2
from scipy.interpolate import interp2d
from tools.array_random_concat import array_random_concat
count= 0
def warpimg(img=None,p=None,sz=None,*args,**kwargs):
    global count
# function wimg = warpimg(img, p, sz)
    
#    img(h,w)
#    p(n,6) : mat format
#    sz(th,tw)
    
    
    if (sz == None):
        sz=img.shape
    
    #if (size(p,1) == 1):
    #   p=ravel(p)
    length = len(p)
    w=sz[1]
    h=sz[0]
    n= p.shape[0]
    xx = np.arange(w)-w/2
    yy = np.arange(h)-h/2
    x,y = np.meshgrid(xx,yy)
    item_1 = np.concatenate((np.ones((h*w,1)),x.reshape(-1,1),y.reshape(-1,1)),axis=1)
    #
    item_2 = np.array([p[:,0:2],p[:,2:4],p[:,4:6]])
    item_2 = np.reshape(item_2,[3,2*length])

    #pos
    pos = np.matmul(item_1,item_2)
    pos = pos.reshape((h,w,n,2))
    target_sz = sz +[len(p)]
    img_w,img_h =img.shape
    func_interp2d = interp2d(np.arange(0,img_h),np.arange(0,img_w),img,kind="linear")
    wimg = None
    #when the length of the p  >1 means it is to warping for  a set of detections 
    if len(p) > 1:
        for  i in range(0,pos.shape[2]):
            single_wimg = func_interp2d(pos[0,:,i,0].flatten(),pos[:,0,i,1].flatten())
            wimg = array_random_concat(wimg,single_wimg,3,2)
    else:
        wimg = func_interp2d(pos[0,:,:,0].flatten(),pos[:,0,:,1].flatten())
    wimg = wimg.reshape(target_sz)
    #get the warp by interp get the [x,y,(w/2),h]patch
    #wimg = scipy.ndimage.map_coordinates(img, [pos[:,:,:,0].flatten(), pos[:,:,:,1].flatten()], order=0, mode='constant').reshape(target_sz)
    #img1 = np.arange(1,31).reshape([5,6])
    #print(img1)
    #x,y = np.meshgrid(np.arange(2,4)- 1.5,np.arange(3,6) - 1.5)
    #f = interp2d(np.arange(0,img1.shape[1]),np.arange(0,img1.shape[0]),img1,kind="linear")
    #wimg1 = f(x[0],y[:,0])
    #print(x[0],"\n",y[:,0])
    #print(wimg1)
    if True:
        #temp_img = func_interp2d(np.arange(0,img.shape[0]),np.arange(0,img.shape[1]))
        count = count+1
        temp_img = wimg*255
        for i in range(0,len(p)):
            cv2.imwrite("./mark/test/test_warp{}.jpg".format(count),temp_img[:,:,i])
            #print("temp_img generated")
    #wimg = ((np.arange(0,target_sz[0]*target_sz[1]*target_sz[2]))%255).reshape(target_sz)
    #wimg[find(isnan(wimg))]=0
    return wimg
