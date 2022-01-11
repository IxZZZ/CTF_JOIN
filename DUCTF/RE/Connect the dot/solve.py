import random

dword_4060 = [65407, 60999, 31620, 5074, 27425, 53858, 20942, 3721]

arr_v8 = [0,1,2,3,4,5,6]


arr_su = [0, 1, 2, 3, 4, 5, 6, 7]
res = 0
count = 5
while True:
    res = 0
    for i in arr_su:
        res = dword_4060[i] ^ (dword_4060[i] >> 8) & res
    res = res & 0xff
    if res == 0xff:
        print(arr_su)
        break
    random.shuffle(arr_su)


# arr_destination = [6, 3, 7, 5, 1, 4, 0, 2]


