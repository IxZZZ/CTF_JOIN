from z3 import *
n = 80
input = [BitVec(f'input_{i}', 32) for i in range(n)]
arr_next = []
for k in range(n >> 2):
    v5 = input[4*k]+91*(91*(input[4*k+2]+91*input[4*k+3])+input[4*k+1])
    arr_next.append(v5 & 0xff)
    v5 = v5 >> 8
    arr_next.append(v5 & 0xff)
    v5 = v5 >> 8
    arr_next.append(v5 & 0xff)
    v5 = v5 >> 8
    arr_next.append(v5 & 0xff)

ans = [24, 50, 104, 2, 213, 84, 140, 4, 66, 247, 82, 4, 163, 127, 54, 2, 108, 105, 100, 5, 68, 86, 82, 4, 192, 17, 26, 3, 86, 114, 255, 4, 52, 147, 52, 2, 241, 41, 58, 2,
       159, 153, 182, 4, 161, 1, 20, 5, 76, 2, 44, 5, 48, 132, 126, 4, 102, 101, 10, 5, 154, 223, 149, 4, 156, 201, 255, 4, 109, 105, 82, 4, 177, 246, 78, 4, 245, 37, 150, 4]

S = Solver()

for i in range(len(ans)):
    S.add(arr_next[i] == ans[i])
    S.add(input[i] >= 32, input[i] <= 126)

assert sat == S.check()

print(S.model())

for i in input:
    print(chr(S.model()[i].as_long()),end='')

#p455w0rd_1s_5tr0n6_wh3n_1t_D03snt_c0nt41n_This_program_cannot_be_run_in_DOS_mode
