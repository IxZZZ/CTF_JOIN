from numpy import random


def ShAr(num, shift, bit=32):
    num = num & int('1'*bit, 2)
    binary = bin(num)[2:]
    prefix = 0
    if len(binary) == 32 and binary[0] == '1':
        prefix = int('1'*shift, 2) << (32-shift)
    return (num >> shift) | prefix


def gen_const(v4, cal_const):
    a1 = (ShAr(v4[2], cal_const[0])+v4[0]) & 0xffffffff

    a2 = (cal_const[1]*v4[3] + cal_const[2]*v4[0]) & 0xffffffff

    a3 = v4[0]
    const_1 = [v4[1], v4[2], (cal_const[3]*a1+cal_const[4]*a2) & 0xffffffff,
               (cal_const[5]*a2+a3) & 0xffffffff, a2]
    print('const_cal: ', cal_const, end='   ')
    print('out constant: ', const_1)
    print([hex(i) for i in const_1])
    return const_1


flag = 'Wanna.One{y0u_4r3_r34lly_l0v3_y0ur_d4ddy_s0_much!1Hy*gWa9R7i#eb}'
# flag = 'R3v_3n9_By_4N9r!'


key = [ord(i) for i in flag]

v6 = [((((((key[4 * i + 3] << 8) + key[4 * i + 2])
         << 8) + key[4 * i + 1]) << 8) + key[4 * i]) & 0xffffffff for i in range(len(flag)//4)]


v5 = []
for i in range(len(v6)):
    v24 = (((ShAr(v6[i], 3) & 0x20000000) + 32 * v6[i]) ^ v6[i])
    v23 = v24 ^ (v24 << 7)
    v22 = (0xff & ShAr(v23, 1)) + v23
    v21 = v22 ^ ((ShAr(v22, 3) & 0x20000000) + 32 * v22)
    v5.append(v21)


v4 = []
for j in range(len(v5)):
    v8 = (v5[j] ^ (v5[j] << 7)) & 0xffffffff
    v7 = ((0xff & ShAr(v8, 1)) + v8) & 0xffffffff
    v4.append(v7)

print(len(v4))

arr_const_cal = []
arr_const_final = []
for i in range(0, len(v4), 4):
    random_const = random.randint(1, 10, size=(6))
    arr_const_cal.append(list(random_const))
    arr_const_final.append(gen_const(v4[i:i+4], random_const))

print()
print()
print(arr_const_cal)
print(arr_const_final)
