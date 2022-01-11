def extract_byte_n(num, n):
    num = (num << ((7-n)*8)) & 0xffffffffffffffff
    num = num >> ((7)*8)
    return num


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


def strip_90(str):
    # str = str.rstrip('4983c1').rstrip('4983').rstrip('49')
    index = str.find('90')

    if index != -1 and index % 2 == 0:
        return reverse_order(str[:index])
    return reverse_order(str)


# len 800
original_offset_rbx = 0x400176
offset_rbx = original_offset_rbx

# len 32 bytes
offset_func = 0x4000AD

arr_func = []

for i in range(4):
    b = ida_bytes.get_bytes(offset_func+8*i, 8)
    b_i = int.from_bytes(b, byteorder='little')
    arr_func.append(b_i)
    # print(hex(arr_func[i]))

# print()

arr_bin = []
input = 'A'*1
bin_tree = ''
for c in input:
    bin_tree += f'{ord(c):08b}'[::-1]

bin_tree = bin_tree + (801-len(bin_tree))*'0'



sum = 0
count = 0
for b_node in bin_tree:
    count += 1
    arr_sub = []
    arr_rbx = []
    for j in range(4):
        b = ida_bytes.get_bytes(offset_rbx+8*j, 8)
        b_i = int.from_bytes(b, byteorder='little')
        arr_rbx.append(b_i)
        # print(hex(arr_rbx[j]))
    # print()

    for i in range(4):
        arr_func[i] ^= arr_rbx[i]
        # print(hex(arr_func[i]))

    str_h = ''
    for h in arr_func:
        str_h += reverse_order(hex(h)[2:], True)
    if count > 340:
        print(str_h)
    index_jump_1 = str_h.find('488d')+6
    arr_sub.append(int(strip_90(str_h[index_jump_1:index_jump_1+8]), 16))
    str_h = str_h[index_jump_1:]

    index_add_1 = str_h.find('83c1')+4
    arr_sub.append(int(str_h[index_add_1:index_add_1+2], 16))
    str_h = str_h[index_add_1:]

    index_jump_2 = str_h.find('488d')+6
    arr_sub.append(int(strip_90(str_h[index_jump_2:index_jump_2+8]), 16))
    str_h = str_h[index_jump_2:]

    index_add_2 = str_h.find('83c1')+4
    arr_sub.append(int(str_h[index_add_2:index_add_2+2], 16))
    str_h = str_h[index_add_2:]

    if index_add_1 == 3 or index_add_2 == 3 or index_jump_1 == 5 or index_jump_2 == 5:
        print('wrong')
        print(str_h)
        print(count)
        break
    arr_bin.append(arr_sub)
    # print(b)
    if b_node == '1':
        offset_rbx = original_offset_rbx + arr_sub[0]
        sum += arr_sub[1]
    else:
        offset_rbx = original_offset_rbx + arr_sub[2]
        sum += arr_sub[3]

    # for h in arr_sub:
    #     print(hex(h), end=' ')
    # print(hex(sum))

print(hex(sum))


# print(arr_bin)

# for i in arr_bin[0]:
#     print(hex(i), end=' ')
