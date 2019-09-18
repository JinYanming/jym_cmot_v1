def mot_count_ids(Tracklet,param):
    id_list = Tracklet.hyp.ystates_ids

    count = 0
    prev_id = id_list[0]
    for i in range(1,len(id_list)):
        cur_id = id_list[i]
        if cur_id != prev_id and cur_id != -1:
            count +=1
            prev_id = cur_id
    param.ids += 1
