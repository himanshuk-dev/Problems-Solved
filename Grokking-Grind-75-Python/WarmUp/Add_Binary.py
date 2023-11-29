# Add Binary Strings
# two binary strings: str1, str2
# 1 ≤ str1.length , str2.length ≤ 500
# str1 and str2 consist of 0 or 1 characters only.
# Any string must not contain leading zeros except the string representing the binary form of 0.
# Examples:
#   str1 = "1"
#   str2 = "1"
#   result: "10"

# Approach
#  Iterate over the two strings in reverse order using two pointers.
#  For each iteration, retreive corresponding digits of the two strings.
#  Sum the retreived digits and carry. Convert the sum to binary and append it to the result.calculate the carry for next iteration.
#  If carry is equal to 1, append it to the result.
#  Reverse the result and return it.


def add_binary(str1, str2):
    result = ""
    pointer1 = len(str1) - 1
    pointer2 = len(str2) - 1
    carry = 0
    while pointer1 >= 0 or pointer2 >= 0:
        sum = carry
        if pointer1 >= 0:
            sum += int(str1[pointer1])
            pointer1 -= 1
        if pointer2 >= 0:
            sum += int(str2[pointer2])
            pointer2 -= 1
        carry = sum // 2
        result = str(sum % 2) + result
    if carry == 1:
        result =  "1" + result
    return result