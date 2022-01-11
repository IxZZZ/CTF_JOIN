from z3 import *

const_arr = [10, 41, 91, 71, 61, 41, 51, 19, 101, 111, 121, 201, 31, 51, 31, 31, 41, 51, 111, 221,
             211, 12, 12, 31, 81, 71, 51, 61, 71, 41, 51, 61, 32, 42, 52, 92, 65, 51, 17, 19, 160, 60, 64, 0]

for i in range(32):
    const_arr[i] = ~const_arr[i]

in_rc4_str = []
for i in range(256):
    in_rc4_str.append(i)

input = [BitVec(f'input_{i}', 8) for i in range(32)]

temp = 0
# print(in_rc4_str)
for i in range(256):
    k = (input[i % len(input)] + in_rc4_str[i] + temp) % 256
    t = in_rc4_str[i]
    in_rc4_str[i] = in_rc4_str[k]
    in_rc4_str[k] = t


v6 = 0
v5 = 0
for i in range(0x20):
    v6 = (v6+1) % 256
    v5 = (in_rc4_str[v6]+v5) % 256
    temp = in_rc4_str[v6]
    in_rc4_str[v6] = in_rc4_str[v5]
    in_rc4_str[v5] = temp
    const_arr[i] = [(
        in_rc4_str[v5]+in_rc4_str[v6]) % 256] ^ const_arr[i]


S = Solver()

for i in range(0x20):
    S.add(const_arr[i] == 255)

print(S)

assert sat == S.check()
