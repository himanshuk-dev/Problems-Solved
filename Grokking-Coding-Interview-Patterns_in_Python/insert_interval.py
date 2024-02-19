# [[6,9]] , [1,5] => [[1,5], [6,9]]
# [[2,7], [9,15], [18, 21]], [5,8] => [[2,8], [9,15], [18, 21]]
#  empty? yes
# sorted? yes
# 
# 1. iterate through intervals
    # 2. if start of current interval is less than start of new interval, append to output list
    # 3. now check if there is overlap between last added interval and new interval
    #       if yes, merge intervals by updating end of current interval
    #       else, append new interval to output
    # 4. now check if there is overlap between last added interval and current interval
    #       if yes, merge intervals by updating end of last added interval
    #       else, append current interval to output
# return output


def insert_interval(existing_intervals, new_interval):
    output = []
    i = 0
    # Add all intervals before the new interval
    while i < len(existing_intervals) and existing_intervals[i][1] < new_interval[0]:
        output.append(existing_intervals[i])
        i += 1
    # Merge intervals that overlap with the new interval
    while i < len(existing_intervals) and existing_intervals[i][0] <= new_interval[1]:
        new_interval = [min(existing_intervals[i][0], new_interval[0]),
                        max(existing_intervals[i][1], new_interval[1])]
        i += 1
    # Add the merged interval
    output.append(new_interval)
    # Add the rest of the intervals
    while i < len(existing_intervals):
        output.append(existing_intervals[i])
        i += 1
    return output