# set two pointers i, j
# loop over both lists
# calculate latest start and ealiest end
# if start is less than end, store these as intersactions
#  if end of list a is less than end of list b
# increment i else j

def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i = j = 0

    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])

        if start <= end:    
            intersections.append([start, end])   

        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1

    return intersections