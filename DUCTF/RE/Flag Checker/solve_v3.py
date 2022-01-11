from z3 import *
# first_func()


def test_first_func():
    flag = [0x41]*36

    v2 = [0]*6
    v3 = [0]*6
    v4 = [0]*6
    v5 = [0]*6
    v6 = [0]*6
    v7 = [0]*6

    v2[0] = 0
    v2[1] = 1
    v2[2] = 2
    v2[3] = 6
    v2[4] = 12
    v2[5] = 18
    v3[0] = 3
    v3[1] = 4
    v3[2] = 5
    v3[3] = 11
    v3[4] = 17
    v3[5] = 23
    v4[0] = 7
    v4[1] = 8
    v4[2] = 9
    v4[3] = 13
    v4[4] = 14
    v4[5] = 15
    v5[0] = 10
    v5[1] = 16
    v5[2] = 22
    v5[3] = 28
    v5[4] = 29
    v5[5] = 35
    v6[0] = 19
    v6[1] = 20
    v6[2] = 24
    v6[3] = 25
    v6[4] = 26
    v6[5] = 30
    v7[0] = 21
    v7[1] = 27
    v7[2] = 31
    v7[3] = 32
    v7[4] = 33
    v7[5] = 34
    # flag = [BitVec(f'flag_{i}', 8) for i in range(36)]

    flag = cal(flag, v2)
    flag = cal(flag, v3)
    flag = cal(flag, v4)
    flag = cal(flag, v5)
    flag = cal(flag, v6)
    flag = cal(flag, v7)
    for i in flag:
        print(hex(i), end=',')


def sub_cal(a1):
    return ((2*a1) ^ (27*((a1 >> 7))))


def cal(a1, a2):
    v9 = a1[a2[0]]
    v10 = a1[a2[1]]
    v11 = a1[a2[2]]
    v12 = a1[a2[3]]
    v13 = a1[a2[4]]
    v14 = a1[a2[5]]

    v2 = v11 ^ v9 ^ sub_cal(v9)
    v3 = sub_cal(v11) ^ v2
    v15 = v3 ^ sub_cal(v13)
    v4 = sub_cal(v10)
    v5 = sub_cal(v12) ^ v12 ^ v10 ^ v4
    v16 = v5 ^ sub_cal(v14)
    v17 = v13 ^ sub_cal(v9)
    v18 = v14 ^ sub_cal(v10)
    v6 = v9 ^ sub_cal(v9)
    v19 = v6 ^ sub_cal(v11)
    v7 = v10 ^ sub_cal(v10)
    v20 = v7 ^ sub_cal(v12)
    a1[a2[0]] = v15
    a1[a2[1]] = v16
    a1[a2[2]] = v17
    a1[a2[3]] = v18
    a1[a2[4]] = v19
    a1[a2[5]] = v20
    return a1


def first_func(flag):
    arr = []
    for i in range(len(flag)):
        arr.append(flag[i])

    v2 = [0]*6
    v3 = [0]*6
    v4 = [0]*6
    v5 = [0]*6
    v6 = [0]*6
    v7 = [0]*6

    v2[0] = 0
    v2[1] = 1
    v2[2] = 2
    v2[3] = 6
    v2[4] = 12
    v2[5] = 18
    v3[0] = 3
    v3[1] = 4
    v3[2] = 5
    v3[3] = 11
    v3[4] = 17
    v3[5] = 23
    v4[0] = 7
    v4[1] = 8
    v4[2] = 9
    v4[3] = 13
    v4[4] = 14
    v4[5] = 15
    v5[0] = 10
    v5[1] = 16
    v5[2] = 22
    v5[3] = 28
    v5[4] = 29
    v5[5] = 35
    v6[0] = 19
    v6[1] = 20
    v6[2] = 24
    v6[3] = 25
    v6[4] = 26
    v6[5] = 30
    v7[0] = 21
    v7[1] = 27
    v7[2] = 31
    v7[3] = 32
    v7[4] = 33
    v7[5] = 34

    a = cal(arr, v2)
    b = cal(a, v3)
    c = cal(b, v4)
    d = cal(c, v5)
    e = cal(d, v6)
    f = cal(e, v7)
    return f


# test_first_func()

swap = [23, 16, 19, 12, 31, 24, 17, 22, 13, 18, 25, 30, 9, 2, 11, 4, 33,
        26, 3, 8, 5, 10, 27, 32, 21, 14, 35, 28, 7, 0, 15, 20, 29, 34, 1, 6]


arr = [15, 79, 115, 60, 65, 198, 164, 175, 180, 65, 214, 101, 200, 153, 170, 179,
       108, 153, 97, 60, 78, 221, 112, 70, 21, 102, 60, 27, 127, 22, 166, 111, 35, 19, 18, 110]
# arr = [130, 130, 195, 130, 130, 195, 195, 130, 130, 195, 130, 195, 65, 195, 65, 65, 130,
#        65, 65, 130, 130, 130, 195, 65, 195, 195, 65, 130, 195, 65, 65, 195, 195, 65, 65, 65]

# arr = [65, 130, 130, 65, 195, 195, 65, 195, 195, 65, 195, 65, 195, 195, 195, 130, 65, 65,
#        130, 130, 195, 130, 130, 195, 130, 65, 65, 195, 130, 130, 65, 130, 65, 65, 130, 195]
# arr = [220, 195, 130, 220, 94, 94, 94, 31, 31, 31, 220, 220, 94, 65, 94, 0, 130, 130,
#        31, 31, 195, 220, 130, 31, 130, 220, 220, 65, 0, 195, 195, 31, 65, 220, 65, 157]

S = Solver()
flag = [BitVec(f'flag_{k}', 8) for k in range(36)]


arr_flag = []
for i in range(len(flag)):
    arr_flag.append(flag[i])

for i in range(16):

    a = first_func(arr_flag)

    # swap
    next_arr = [0]*36
    for j in range(36):
        next_arr[j] = a[swap[j]]
    a = next_arr

print(a)
for k in range(36):
    S.add(arr[k] == a[k])
    # S.add(flag[k] >= 32, flag[k] <= 128)
    S.add(UGT(flag[k], 32), ULT(flag[k], 127))

assert sat == S.check()
ans = S.model()
arr_res = []
flag = [BitVec(f'flag_{k}', 8) for k in range(36)]
for f in flag:
    arr_res.append(ans[f].as_long())
print(arr_res)

# arr = [15, 79, 115, 60, 65, 198, 164, 175, 180, 65, 214, 101, 200, 153, 170, 179,
#    108, 153, 97, 60, 78, 221, 112, 70, 21, 102, 60, 27, 127, 22, 166, 111, 35, 19, 18, 110]
