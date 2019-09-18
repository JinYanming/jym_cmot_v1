import numpy as np
from Common.color_tools import rgb2hsv
from mot_func.mot_generate_temp import mot_generate_temp
from tools.array_random_concat import array_random_concat
def mot_appearance_model_generation(img=None,param=None,state=None,state_list=False,*args,**kwargs):

    # input :
    # img: a color image
    # state: [Center(X), Center(Y), Width, Height]
    # output : 
    # tmpl_hist: color histograms

    if param.color=='HSV':
        h,s,v = rgb2hsv(img[0],img[1],img[2])
        hsv_img = [h,s,w]
    else:
        hsv_img = img
    
    h_img=hsv_img[:,:,0] / np.max(img[:,:,0])
    s_img=hsv_img[:,:,1] / np.max(img[:,:,1])
    v_img=hsv_img[:,:,2] / np.max(img[:,:,2])
    #v_img=double(hsv_img(arange(),arange(),3)) / double(max(max(img(arange(),arange(),3))))
    initS = state if state_list else [state]
    h_tmpl=mot_generate_temp(h_img,initS,param.tmplsize)
    s_tmpl=mot_generate_temp(s_img,initS,param.tmplsize)
    v_tmpl=mot_generate_temp(v_img,initS,param.tmplsize)
    
    Nd=len(initS)
    h_tmpl = h_tmpl.reshape([param.subvec,param.subregion,Nd])
    s_tmpl = s_tmpl.reshape([param.subvec,param.subregion,Nd])
    v_tmpl = v_tmpl.reshape([param.subvec,param.subregion,Nd])
    all_tmpl = np.ones([3,param.subvec, param.subregion,Nd])
    all_tmpl[0]=h_tmpl#all_tmpl shape [3,2018,1,1]
    all_tmpl[1]=s_tmpl
    all_tmpl[2]=v_tmpl
    nbins=param.Bin
    tmpl_hist=None
    for j in range(0,Nd):
        temp_hist = None
        i = 0
        while i < 3:
            max_val=np.max(np.max(all_tmpl[i,:,:,j]))
            cb_tmpl=all_tmpl[i,:,:,j]
            cb_tmpl=np.dot((cb_tmpl/max_val),nbins)
            if param.subregion == 1:
                #to get the histogram map location
                cb_tmpl_hist=(np.histogram(cb_tmpl,nbins)[0] / param.subvec).T
            else:
                cb_tmpl_hist=(np.histogram(cb_tmpl,nbins)[0] / param.subvec)
            cb_tmpl_hist = cb_tmpl_hist[:,np.newaxis]
            temp_hist = array_random_concat(temp_hist,cb_tmpl_hist,2,0)
            i = i+1
        shape = None if ~ isinstance(tmpl_hist,np.ndarray)  else tmpl_hist.shape
        tmpl_hist = array_random_concat(tmpl_hist,temp_hist/3,3,2)
    return tmpl_hist

