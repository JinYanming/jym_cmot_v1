import numpy as np
from mot_func.mot_color_similarity import mot_color_similarity
from mot_func.mot_motion_similarity import mot_motion_similarity
from mot_func.mot_shape_similarity import mot_shape_similarity


def mot_eval_association_matrix(Refer = None,Test = None,param = None,type_ = None,ILDA = None,*args,**kwargs):

    
    if ILDA.n_update !=  0:
        nproj = size(ILDA.DiscriminativeComponents,2)
    else:
        nproj = 0
    
    # Association score matrix
    score_mat = np.zeros((len(Refer),len(Test)))#generate a matrix with shape [len(tracklet,len(cur_detetcions))] 
    for i in range(0,len(Refer)):
        refer_hist = np.ravel(Refer[i].hist) / sum(np.ravel(Refer[i].hist))
        refer_h = Refer[i].h
        refer_w = Refer[i].w
        for j in range(0,len(Test)):
            # Appearance affinity
            test_hist = np.ravel(Test[j].hist) / sum(np.ravel(Test[j].hist))
            if (param.use_ILDA) and (ILDA.n_update !=  0) and (nproj > 2):
                proj = ILDA.DiscriminativeComponents
                refer_feat = dot(proj.T,refer_hist)
                test_feat = dot(proj.T,test_hist)
                app_sim = dot(refer_feat,test_feat) / (dot(norm(refer_feat),norm(test_feat)))
            else:
                app_sim = mot_color_similarity(refer_hist,test_hist)
            # Motion affinity
            mot_sim = mot_motion_similarity(Refer[i],Test[j],param,type_)
            test_h = Test[j].h
            test_w = Test[j].w
            shp_sim = mot_shape_similarity(refer_h,refer_w,test_h,test_w)
            score_mat[i,j] = np.dot(np.dot(mot_sim,app_sim),shp_sim)
    
    return score_mat
    
if __name__  ==  '__main__':
    pass
    

