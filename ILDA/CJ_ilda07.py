
    
def CJ_ilda07(init_data=None,init_label=None,*args,**kwargs):

    #----------------
    # ILDA pseudocode
    # written by T-K. Kim, 2007
    dataset_1=copy(init_data)
    label_1=copy(init_label)
    
    numOfupdate=length(dataset_1)
    eigenThreshold=1
    for nupdate in arange(0,numOfupdate).reshape(-1):
        if (nupdate == 0):
            # init proc
            m_1,M_1,TeigenVect_1,TeigenVal_1=fGetStModel(dataset_1,eigenThreshold,nargout=4)
            m_1,M_1,BeigenVect_1,BeigenVal_1,samplePerClass_1,meanPerClass_1=fGetSbModel(dataset_1,label_1,eigenThreshold,nargout=6)
            DiscriminativeComponents,D=fGetDiscriminativeComponents(TeigenVect_1,TeigenVal_1,BeigenVect_1,BeigenVal_1,M_1,DeigenThreshold,nargout=2)
        else:
            # for new data
            dataset_2=copy(New_data)
            label_2=copy(New_label)
            m_2,M_2,TeigenVect_2,TeigenVal_2=fGetStModel(dataset_2,eigenThreshold,nargout=4)
            m_2,M_2,BeigenVect_2,BeigenVal_2,samplePerClass_2,meanPerClass_2=fGetSbModel(dataset_2,label_2,eigenThreshold,nargout=6)
            outMean,outNSample,outEVect_t,outEVal_t=fMergeSt(m_1,M_1,TeigenVect_1,TeigenVal_1,m_2,M_2,TeigenVect_2,TeigenVal_2,eigenThreshold,nargout=4)
            outMean,outNSample,outEVect_b,outEVal_b,outSamplePerClass,outMeanPerClass=fMergeSb(m_1,M_1,BeigenVect_1,BeigenVal_1,samplePerClass_1,meanPerClass_1,label_1,m_2,M_2,BeigenVect_2,BeigenVal_2,samplePerClass_2,meanPerClass_2,label_2,eigenThreshold,nargout=6)
            DiscriminativeComponents,D=fGetDiscriminativeComponents(outEVect_t,outEVal_t,outEVect_b,outEVal_b,outNSample,DeigenThreshold,nargout=2)
            m_1=copy(outMean)
            M_1=copy(outNSample)
            TeigenVect_1=copy(outEVect_t)
            TeigenVal_1=copy(outEVal_t)
            BeigenVect_1=copy(outEVect_b)
            BeigenVal_1=copy(outEVal_b)
            samplePerClass_1=copy(outSamplePerClass)
            meanPerClass_1=copy(outMeanPerClass)
            label_1=horzcat(label_1,label_2)
    
    return m,n
    
if __name__ == '__main__':
    pass
    
