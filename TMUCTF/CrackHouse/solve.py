arr_sub = [0, 2, -2, 4, -4, 4, -6, 7, -8, -2, -10,
 -13, -12, -3, -14, -8, 2, 4, 4, 7, -2, -13, -3, -8]



for c in range(78,91):
    username = 'ANANANANANANANAN'
    username = username.replace('N',chr(c))
    license = ''
    for i in range(len(username)):
        license += chr(ord(username[i])-arr_sub[i])
    print('--license--')
    print(username)
    print(license)


arr_sub = [0, -4, -2, -4, -4, -3, -6, -2, -8, -
           10, -10, -1, -12, -14, -14, -16, 2, 4, -2, -3]


for c in range(65, 78):
    username = 'ANANANANANANANAN'
    username = 'ANANANANANANANAN'.replace('N', 'B')
    username = username.replace('B', chr(c))
    license = ''
    for i in range(len(username)):
        license += chr(ord(username[i])-arr_sub[i])
    print('--license--')
    print(username)
    print(license)


arr_sub = [0, -4, -2, -3, -4, 2, -6, 3, -8, 3, -10, 3, -12, 7, -14, 9]


for c in range(97, 110):
    username = 'ANANANANANANANAN'
    username = 'ANANANANANANANAN'.replace('N', 'a')
    username = username.replace('a', chr(c))
    license = ''
    for i in range(len(username)):
        license += chr(ord(username[i])-arr_sub[i])
    print('--license--')
    print(username)
    print(license)


# TMUCTF{W0w_Y0u_Cr4ck3d_7h3_H0u53_L1k3_4_Ch4mp}
