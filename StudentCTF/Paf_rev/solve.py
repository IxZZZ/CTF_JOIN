def reverse_order(str, is_full32=False):
    res = ''
    while len(str) % 2 != 0:
        str = '0'+str
    if is_full32 == True:
        while len(str) != 16:
            str = '0'+str
    str = str[::-1]
    for i in range(0, len(str), 2):
        res += (str[i:i+2])[::-1]
    return res


arr_program = []
for i in range(16096):
    b = ida_bytes.get_bytes(jmp_rip+i,1)
    b_i = int.from_bytes(b,byteorder='little')
    arr_program.append(b)

 
jmp_rip = 0
