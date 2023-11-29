# input: (array, tagretSum)
# output: outputArray []

# *sorting will not matter here anyways



def two_Number_Sum(array, targetSum):
    # set left and right pointers
    leftIdx = 0
    rightIdx = len(array) - 1
  
    # sort the array 
    array.sort()
    
    # loop over array
    while leftIdx < rightIdx:
        currentSum = array[leftIdx] + array[rightIdx]
        
        # check if sum of array[left] + array[right]  === targetSum push these values to outputArray
        if currentSum == targetSum:
            return [array[leftIdx], array[rightIdx]]
            
        # if sum of array[left] + array[right] < target left++
        elif currentSum < targetSum:
            leftIdx += 1
        else:
            # else right--
            rightIdx -= 1
            
    return []