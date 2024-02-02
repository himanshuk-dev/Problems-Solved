# String to integer

# string_to_int(str)
# '- 00030' => -30
# '- 0-051' => 0
# '+101' => 101
#  '+.23' => 0
#  'Tim5' => 0
#  '5rock' => 5
 

# Process >>>
# 1. Remove leading spaces
# 2. check if string value is '-' or '+', if its -, store in variable sign = -1
# 3. Convert digits to integer and check for overflow
#   look over string         
#       convert to int
        # check for overflow
# return the result
# 


def string_to_int(str):
    sign = 1
    Min = -2 ** 31
    Max = 2 ** 31 - 1
    i = 0
    result = 0
    
    # remove leading spaces
    while(i < len(str) and str[i].isspace()):
        i += 1
        
    # check if string is - or +
    while(i < len(str) and (str[i] == '-' or str[i] == '+')):
        if str[i] == '-':
            sign = -1 
        else:
            sign = 1
        
        i += 1
    
    # Convert digits to integer and check for overflow
    while(i < len(str) and str[i].isdigit()):
        
        # covert digit to int
        digit = ord(str[i]) - ord('0')
        
        # check for overflow
        if(result > (Max - digit // 10)):
            return Max if sign == 1 else Min
        
        result = sign * result * 10 + digit
        i+=1
    
    return result