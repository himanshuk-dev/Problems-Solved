# Insert first interval to output array
# Loop over each interval in input list except the first
# if the last interval overlaps, we will merge and return ouput
# otherwise, add the input interval to the outpu list
# 
# sorted? yes
# leng of input >= 1 yes
# integers yes
# 

def merge_intervals(intervals):
    
    if len(intervals) == 0:
        return None
    
    output = [[intervals[0][0], intervals[0][1]]]
    
    for i in range(1, len(intervals)):
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        
        last_added_output = output[len(output) -1 ]
        
        if curr_start <= last_added_output[1]:
             output[-1][1] = max(curr_end, last_added_output[1])
        else:
            output.append([curr_start, curr_end])
            
    return output
        
        
        
        
    
    