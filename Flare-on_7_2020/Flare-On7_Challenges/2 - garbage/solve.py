v12 = [0]*15

v14 = [0]*5

v12[0] = 0x2C332323
v12[1] = 0x49643F0E
v10 = "nPTnaGLkIqdcQwvieFQKGcTGOTbfMjDNmvibfBDdFBhoPaBbtfQuuGWYomtqTFqvBSKdUMmciqKSGZaosWCSoZlcIlyQpOwkcAgw "
v12[2] = 0x40A1E0A
v12[3] = 0x1A021623
v12[4] = 0x24086644
v11 = "KglPFOsQDxBPXmclOpmsdLDEPMRWbMDzwhDGOyqAkVMRvnBeIkpZIhFznwVylfjrkqprBPAdPuaiVoVugQAlyOQQtxBNsTdPZgDH "
v12[5] = 0x2C741132
v12[6] = 0xF422D2A
v12[7] = 0xD64503E
v12[8] = 0x171B045D
v12[9] = 0x5033616
v12[10] = 0x8092034
v12[11] = 0xE242163
v12[12] = 0x58341415
v12[13] = 0x3A79291A
v12[14] = 0x58560000
v13 = 0x54
v14[0] = 0x3B020E38
v14[1] = 0x341B3B19
v14[2] = 0x3E230C1B
v14[3] = 0x42110833
v14[4] = 0x731E1239

def sub_401000(arr,s):
    v9 = []
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(4):
            t = (temp&0xff) ^ ord(s[i*4+j])
            v9.append(t)
            temp >>= 8 
    return v9

v = sub_401000(v14,v11)

print(''.join([chr(i) for i in v]))

v = sub_401000(v12, v10)

print(''.join([chr(i) for i in v]))
