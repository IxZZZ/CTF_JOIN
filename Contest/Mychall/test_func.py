def shift_right_arithm(num, shift, bit=32):
    num = num & int('1'*bit, 2)
    binary = bin(num)[2:]
    prefix = 0
    if len(binary) == 32 and binary[0] == '1':
        prefix = int('1'*shift, 2) << (32-shift)
    return (num >> shift) | prefix
