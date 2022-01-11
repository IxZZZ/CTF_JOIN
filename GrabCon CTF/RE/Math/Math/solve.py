from z3 import *

flag_1 = [BitVec(f"flag1_{i}", 8) for i in range(19)]
flag_2 = [BitVec(f"flag2_{i}", 8) for i in range(19)]

haft_first = 0
haft_last = 0


for i in range(len(flag_1)):
    haft_first = (haft_first << 8) | flag_1[i]
    haft_last = (haft_last << 8) | flag_2[i]


#v5 = int('1eec4819d6e791bb85a2bb67f19eab07e684ffaea9b7a43d8c6e710999c8ad24d82d31c520e77e33c97e7f7bfa8ba6f386bb12b793ee761a520ce3936184cccf32d32c0fef4ee5b9dbedc890a7463687d', 16)
v5 = 8817764871678636846701748696024572804919275253613183516923518210991784748446775394911505870897688600925721194186789120242813983294872845530102437613810130271412078151212089001942720645733509245

v6 = haft_first
v7 = haft_last

v12 = (v5 - (v7*v7*v7)*v6*0x38FB4974)*5

v13 = (v6*v6*v6*v6)*0x1B46B1 + (v6*v6*v6)*0x11CE86F44 * v7 + \
    (v7*v7)*(v6*v6)*0x2E7FD486126 + (v7*v7*v7*v7)*0x1B46B1



S = Solver()

# GrabCON{
S.add(v12 == v13)
S.add(flag_1[0]==ord('G'))
S.add(flag_1[1]==ord('r'))
S.add(flag_1[2] == ord('a'))
S.add(flag_1[3] == ord('b'))
S.add(flag_1[4] == ord('C'))
S.add(flag_1[5] == ord('O'))
S.add(flag_1[6] == ord('N'))
S.add(flag_1[7] == ord('{'))
S.add(flag_2[18] == ord('}'))
for i in range(len(flag_1)):
    S.add(flag_1[i] >= 48)
    S.add(flag_1[i] <= 126)
    S.add(flag_2[i] >= 48)
    S.add(flag_2[i] <= 126)

print(S)

assert S.check() == sat

ans = S.model()

print(ans)
for i in flag_1:
    print(chr(ans[i].as_long()),end='')

for i in flag_2:
    print(chr(ans[i].as_long()), end='')
