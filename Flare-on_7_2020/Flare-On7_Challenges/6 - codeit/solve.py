with open('sprite.bmp', 'rb') as file:
    data = file.read()[54:]
for d in range(0, 7*20, 7):
    res = 0
    for i in range(6, -1, -1):
        res += (data[d] & 1) << i
        d += 1
    print(chr(res), end='')


# L00ks_L1k3_Y0u_D1dnt_Run_Aut0_Tim3_0n_Th1s_0ne!@flare-on.com
