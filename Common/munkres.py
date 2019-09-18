import numpy as np
from Obj.hungarian import Hungarian
def munkres(score_mat):
    hungarian = Hungarian(score_mat)
    hungarian.calculate()
    result = hungarian.get_results()
    assignment = np.zeros(score_mat.shape)
    cost = hungarian.get_total_potential()
    for point in result:
        r,c = point
        assignment[r,c] = 1
    return assignment,cost
