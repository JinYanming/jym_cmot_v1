import numpy as np
def ListIndice1d(raw_list,indice_list):
    result_list = []
    for item in indice_list:
        result_list.append(raw_list[item])
    return result_list

def ListIndice2d(raw_list = None,indice_list_row = None,indice_list_col = None):
    result_list = []
    if indice_list_row == None:
        indice_list_row = [0,len(raw_list)]
    for i in range(indice_list_row[0],indice_list_row[1]):
        result_list.append(raw_list[i][indice_list_col[0]:indice_list_col[1]])
    return result_list

def ListInsert(raw_list,insert_indice,value = None,padding = None):
    """
    to assign the list what ever the indice is in range(0,length or not),and auto pad with padding values
    """
    length = len(raw_list)
    if insert_indice+1 <= length:
        raw_list[insert_indice] = value
    else:
        for i in range(length,insert_indice):
            raw_list.append(padding)
        raw_list.append(value)

