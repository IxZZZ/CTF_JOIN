from z3 import *
from Crypto.Util.number import long_to_bytes


def displace(a, base):
    res = []
    for i in range(base):
        if base + i >= len(a):
            for j in range(base - 1, i - 1, -1):
                res.append(a[j])
            return res
        res.append(a[base + i])
        res.append(a[i])
    for j in range(len(a) - 1, 2 * base - 1, -1):
        res.append(a[j])
    return res


file = open('output.txt', 'r')

bytes_arr = long_to_bytes(file.read())
n = 120
print(n)
flag = [BitVec(f'flag_{i}', 8) for i in range(n)]

encoded_flag = []

for i in range(n):
    encoded_flag.append(flag[i] ^ flag[i - 1])

for i in range(n):
    encoded_flag[i] ^= encoded_flag[n - i - 1]
a = []

for i in range(0, n, 3):
    a.append(encoded_flag[i] + encoded_flag[i + 1])
    a.append(encoded_flag[i + 1] + encoded_flag[i + 2])
    a.append(encoded_flag[i + 2] + encoded_flag[i])


encoded_flag = a
for i in range(1, n):
    if i % 6 == 0:
        encoded_flag = displace(encoded_flag, i)

S = Solver()

for i in range(len(bytes_arr)):
    # const = int.from_bytes(bytes_arr[i], byteorder='little')

    S.add(encoded_flag[i] == bytes_arr[i])

print(bytes_arr)

for i in range(len(flag)):
    S.add(flag[i] >= 0, flag[i] <= 128)

print(S)
assert sat == S.check()
