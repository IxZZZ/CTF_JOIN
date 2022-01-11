from z3 import *

key = [BitVec(f"key_{i}", 32) for i in range(16)]


v6 = [((((((key[4 * i + 3] << 8) + key[4 * i + 2])
         << 8) + key[4 * i + 1]) << 8) + key[4 * i]) & 0xffffffff for i in range(4)]

print(v6)


v24 = ((((v6[0] >> 3) & 0x20000000) + 32 * v6[0]) ^ v6[0])
v23 = v24 ^ (v24 << 7)
v22 = (0xff & (v23 >> 1)) + v23
v21 = v22 ^ (((v22 >> 3) & 0x20000000) + 32 * v22)


v20 = ((((v6[1] >> 3) & 0x20000000) + 32 * v6[1]) ^ v6[1])
v19 = v20 ^ (v20 << 7)
v18 = (0xff & (v19 >> 1)) + v19
v17 = v18 ^ (((v18 >> 3) & 0x20000000) + 32 * v18)


v16 = (((v6[2] >> 3) & 0x20000000) + 32 * v6[2]) ^ v6[2]
v15 = v16 ^ (v16 << 7)
v14 = (0xff & (v15 >> 1)) + v15
v13 = v14 ^ (((v14 >> 3) & 0x20000000) + 32 * v14)


v12 = (((v6[3]>> 3) & 0x20000000) + 32 * v6[3]) ^ v6[3]
v11 = v12 ^ (v12 << 7)
v10 = ((0xff & (v11 >> 1)) + v11) & 0xffffffff
v9 = v10 ^ (((v10>> 3) & 0x20000000) + 32 * v10)
v9 = v9 & 0xffffffff


v5 = [v21, v17, v13, v9]


v4 = []
for j in range(4):
    v8 = (v5[j] ^ (v5[j] << 7)) & 0xffffffff
    v7 = ((0xff & (v8 >> 1)) + v8) & 0xffffffff
    v4.append(v7)

S = Solver()

S.add(v4[1] == 0xF23A4BDA)

S.add(v4[2] == 0xD5EAE2D4)


a1 = ((v4[2] >> 2)+v4[0]) & 0xffffffff

a2 = (2*v4[3] + 2*v4[0]) & 0xffffffff

a3 = v4[0]

S.add((((4*a1) & 0xffffffff) + ((2*a2) & 0xffffffff)) == 0xC6630150)

S.add((2*a2+a3) & 0xffffffff == 0xE429D014)

S.add(a2 == 0x455D304E)

for i in range(len(key)):
    S.add(key[i] >= 33, key[i] <= 128)
assert S.check() == sat

ans = S.model()
print(ans)
for i in key:
    print(chr(ans[i].as_long()), end='')
