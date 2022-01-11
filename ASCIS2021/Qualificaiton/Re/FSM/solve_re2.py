from z3 import *

arr = [0xEE4A5A9, 0x3B51B17B, 0xA0C60127,
       0xBE0CB343, 0xF7AA25A5, 0xC436BB95, 0xD51C1EE8, 0xCAD35653, 0x24B89A46, 0xBD]
arr_final = []

arr_s = [0xD071705, 0x76747617, 0x75]
s = []
for a in arr:
    while a:
        arr_final.append(a & 0xff)
        a = a >> 8

for a in arr_s:
    while a:
        s.append(a & 0xff)
        a = a >> 8
# print(arr_final)
print(len(arr_final))
print(len(s))

print(arr_final)
print(s)

for i in range(len(s)):
    s[i] = s[i]^0x28^0x6c

ascii_build = [i for i in range(256)]

v7 = 0
for j in range(256):
    v7 = (ascii_build[j]+v7+s[j % len(s)]) % 256
    v5 = ascii_build[j]
    ascii_build[j] = ascii_build[v7]
    ascii_build[v7] = v5

print(ascii_build)
v11 = 0
v8 = 0

v28 = [0 for i in range(37)]

input = [BitVec(f'input_{i}', 8) for i in range(37)]

# input = []
# str_input = 'ASCIS{' + 'a'*31
# for i in range(37):
#     input.append(ord(str_input[i]))


for i in range(37):
    v11 = (v11+1) % 256
    v8 = (v8+ascii_build[v11]) % 256
    v6 = ascii_build[v11]
    ascii_build[v11]  = ascii_build[v8]
    ascii_build[v8] = v6
    v28[i] = ascii_build[(ascii_build[v11]+ascii_build[v8]) & 0xff] ^ input[i]

# print(v28)

# for i in v28:
#     print(hex(i),end=' ')
S = Solver()
for i in range(37):
    S.add(v28[i] == arr_final[i])


for item in input:
    S.add(item >= 32, item <= 127)


assert sat == S.check()

ans = S.model()
res = ''.join(chr(ans[i].as_long()) for i in input)
print(res)
# print(ans)
