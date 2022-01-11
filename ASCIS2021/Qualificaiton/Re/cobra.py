from pwn import *
import numpy as np
import cv2

r = remote('125.235.240.166', 20123)

while True:
    data = r.recv()
    print(data.decode('utf-8'))

    data = data.split(b'\n')[2:-1]

    s = []
    for line in data:
        line = line.strip()
        s1 = []
        s2 = []
        i = 0
        while i < len(line):
            if line[i] == 0xc2:
                s1.append((255, 255, 255))
                s2.append((255, 255, 255))
                i += 2
            elif line[i] == 0xe2:
                if line[i + 2] == 0x84:
                    s1.append((255, 255, 255))
                    s2.append((0, 0, 0))
                elif line[i + 2] == 0x80:
                    s1.append((0, 0, 0))
                    s2.append((255, 255, 255))
                else:
                    s1.append((0, 0, 0))
                    s2.append((0, 0, 0))
                i += 3
            else:
                print(line[i])
                exit(0)
        s.append(s1)
        s.append(s2)

    image = np.array(s).astype(np.uint8)
    cv2.imwrite('color_img.png', image)
    '''
    cv2.imwrite('color_img.png', image)

    detector = cv2.QRCodeDetector()

    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error")
    '''
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # scale_im = cv2.resize(image, (0, 0), fx=5, fy=5)
    scale_im = image
    # detect and decode
    cv2.imwrite('color_img.png', scale_im)
    data, vertices_array, binary_qrcode = detector.detectAndDecode(scale_im)
    '''
    data = decode(image)
    '''
    print(data)
    #print(data.data)
    z = data.strip().split('|')

    r.sendlineafter(b'ID Number: ', bytes(z[0], 'utf-8'))
    r.sendlineafter(b'ID Number: ', bytes(z[1], 'utf-8'))
    r.sendlineafter(b'ID Number: ', bytes(z[2], 'utf-8'))
