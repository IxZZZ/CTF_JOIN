from z3 import *


def gen_const(v4, cal_const):
    # SIGWINCH
    a1 = ((v4[2] >> cal_const[0])+v4[0]) & 0xffffffff
    # SIGSYS
    a2 = (cal_const[1]*v4[3] + cal_const[2]*v4[0]) & 0xffffffff

    a3 = v4[0]

    
    const_1 = [v4[1], v4[2], (cal_const[3]*a1+cal_const[4]*a2) & 0xffffffff,
               (cal_const[5]*a2+a3) & 0xffffffff, a2]
    return const_1


key = [BitVec(f"key_{i}", 32) for i in range(64)]

# SIGTRAP
v6 = [((((((key[4 * i + 3] << 8) + key[4 * i + 2])
         << 8) + key[4 * i + 1]) << 8) + key[4 * i]) & 0xffffffff for i in range(len(key)//4)]

v5 = []
for i in range(len(v6)):
    # SIGFPE
    v24 = ((((v6[i] >> 3) & 0x20000000) + 32 * v6[i]) ^ v6[i])
    v23 = v24 ^ (v24 << 7)

    # SIGCONT
    v22 = ((0xff & (v23 >> 1)) + v23)
    v21 = v22 ^ (((v22 >> 3) & 0x20000000) + 32 * v22)
    v5.append(v21)

v4 = []
# SIGILL
for j in range(len(v5)):
    v8 = (v5[j] ^ (v5[j] << 7)) & 0xffffffff
    v7 = ((0xff & (v8 >> 1)) + v8) & 0xffffffff
    v4.append(v7)

S = Solver()

v4_const = [[4168099905, 3460811466, 3166149980, 1926604705, 829546058], [3888838837, 3549494509, 834302606, 4187959490, 522221212], [
    2783117493, 3710170029, 3759869023, 340280210, 1711963366], [4025500862, 969913447, 2943343419, 2060407396, 1464290225]]

cal_const = [[3, 9, 4, 8, 6, 7], [3, 2, 4, 6, 7, 6],
             [2, 1, 3, 9, 5, 6], [8, 4, 9, 8, 3, 3]]

for i in range(len(cal_const)):
    const_1 = gen_const(v4[i*4:4*i+4], cal_const[i])
    for j in range(len(v4_const)):
        S.add(const_1[j] == v4_const[i][j])


for i in range(len(key)):
    S.add(key[i] >= 32, key[i] <= 126)
assert S.check() == sat

ans = S.model()
# print(ans)
for i in key:
    print(chr(ans[i].as_long()), end='')
