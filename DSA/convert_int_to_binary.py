from stack import Stack


def convert_int_to_bin(dec_num):
    s = Stack()

    if dec_num == 0:
        return 0
    
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
        
    bin = ''
    while not s.is_empty():
        bin += s.pop()
        
    return bin