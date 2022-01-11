from z3 import *


def solve_func_1_2(con_1, con_2, con_3, con_4, res_1, res_2):
    b = BitVec('b', 128)

    check_1 = LShR(
        (((con_1*b) & 0xffffffffffffffff)*con_2), 64) & 0x3ffff
    check_2 = LShR(
        (((con_3*b) & 0xffffffffffffffff)*con_4), 64) & 0x3ffff
    S = Solver()
    S.add(check_1 == res_1, check_2 == res_2, b > 0, b <= 0xffffffff)

    assert sat == S.check()

    ans = S.model()

    print(ans)


def solve_func_3_4(con_1, con_2, con_3, res):
    b = BitVec('b', 128)

    check_1 = (b*con_1) & 0xffffffffffffffff

    check_2 = LShR(((b*con_2) & 0xffffffffffffffff)*con_3, 64) & 0x3ffff
    S = Solver()
    S.add(check_1 < con_1, check_2 == res, b > 0, b <= 0xffffffff)

    assert sat == S.check()

    ans = S.model()

    print(ans)


arr_cons = [[0x5F50DDCA7B17, 0x2AF91, 0x4DC4591DAC8F, 0x34AB9, 0x9569, 0x26CF2], [
    0x4AE11552DF1A, 0x36B39, 0x46680B140EFF, 0x3A2D3, 0x20468, 0x3787A]]
arr_con_af = [[0x4D935BBD3E0, 0x66B9B431B9ED,
               0x27DF9, 0x5563], [0x1E5D2BE81C5, 0x448626500938, 0x3BC65, 0x133E7]]


for arr_con in arr_cons:
    solve_func_1_2(arr_con[0], arr_con[1], arr_con[2],
               arr_con[3], arr_con[4], arr_con[5])

for arr_con in arr_con_af:
    solve_func_3_4(arr_con[0], arr_con[1], arr_con[2],
                   arr_con[3])
# [b = 772928896]
# [b = 2204180909]
# [b = 4273479145]
# [b = 1334930147]