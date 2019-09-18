import numpy as np
def array_random_concat(array_to_added = None,array_to_add = None,target_shape_length = 0,concat_dims = None):
    dims_matched = lambda a,b: True if len(a.shape)==len(b.shape) else False
    if isinstance(array_to_added,np.ndarray) == False:
        if target_shape_length > len(array_to_add.shape):
            expanded_array_to_add = np.expand_dims(array_to_add,axis=concat_dims)
            result_array = expanded_array_to_add
        else:
            result_array = array_to_add
    else:
        dims_target = [i for i in range(0,target_shape_length)]
        dims_exist = [i for i in range(0,len(array_to_added.shape))]
        if dims_matched(array_to_added,array_to_add):
            if len(array_to_added.shape) == target_shape_length:
                result_array = np.concatenate((array_to_added,array_to_add),axis=concat_dims)
            else:
                expanded_array_to_added = np.expand_dims(array_to_added,axis=concat_dims)
                expanded_array_to_add = np.expand_dims(array_to_add,axis=concat_dims)
                result_array = np.concatenate((array_to_added,array_to_add),axis=concat_dims)
        else:
            if len(array_to_added.shape) == target_shape_length:
                expanded_array_to_add = np.expand_dims(array_to_add,axis=concat_dims)
                result_array = np.concatenate((array_to_added,expanded_array_to_add),axis=concat_dims)
            else:
                expanded_array_to_added = np.expand_dims(array_to_added,axis=concat_dims)
                result_array = np.concatenate((expanded_array_to_added,array_to_add),axis=concat_dims)
    return result_array

if __name__ == "__main__":
    a = np.zeros([3,4,1,3])
    b = np.zeros([3,4,1,3])
    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[11,22,33],[44,55,66]])
    c = array_random_concat(a,b,2,1)
    print(c)
