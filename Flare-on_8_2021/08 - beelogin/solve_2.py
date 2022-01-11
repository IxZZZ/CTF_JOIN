import base64
from z3 import *

file = open('solve_payload2.txt', 'r')

str = file.read()

str_decoded_constant_1 = base64.b64decode(str)

str_decoded_constant_2 = base64.b64decode(
    "N0l2N2l2RTVDYlNUdk5UNGkxR0lCbTExZmI4YnZ4Z0FpeEpia2NGN0xGYUh2N0dubWl2ZFpOWm15c0JMVDFWeHV3ZFpsd2JvdTVSTW1vZndYRGpYdnhrcGJFS0taRnZOMnNJU1haRXlMM2lIWEZtN0RSQThoMG8yYUhjNFZLTGtmOXBDOFR3OUpyT2RwUmFOOUdFck12bXd2dnBzOUVMWVpxRmpnc0ZHTFFtMGV4WW11Wmc1bWRpZWZ6U3FoZUNaOEJiMURCRDJTS1o3SFpNRzcwRndMZ0RCNFFEZWZsSWE4Vg==")


def decode_64(key):
    res = []
    for i in range(len(key)):
        res.append(
            (str_decoded_constant_1[i]-((str_decoded_constant_2[i] + key[i] & 0xff))) & 0xff)
    return ''.join([chr(i) for i in res])


def decode_full(key):
    res = []
    block_1 = []
    for i in range(len(str_decoded_constant_2)):
        block_1.append((str_decoded_constant_2[i] + key[i % len(key)]) & 0xff)

    for i in range(len(str_decoded_constant_1)):
        res.append((str_decoded_constant_1[i]-block_1[i % len(block_1)])& 0xff)
    file = open('decode_js_2.js','w')
    str_res =  ''.join([chr(i) for i in res])
    file.write(str_res)
    file.close()
    print('Done decode!')


def traversel(arr, str, i, stop):
    if i == stop:
        print(str+'  --> ', decode_64([ord(c)
              for c in "UQ8yjqwAkoVGm7VDdhLoDk0Q75eKKhTfXXke36UF"+str]))
        return
    for o in arr[i]:
        traversel(arr, str+chr(o), i+1, stop)



print(len(str_decoded_constant_1))
print(len(str_decoded_constant_2))

key_arr = [[85], [79, 81], [56], [121], [104, 106], [111, 113], [117, 119], [65], [107], [111], [86], [69, 71], [109], [55], [86], [66, 68], [100], [104], [76], [111], [68], [107], [48], [81], [55], [53], [101], [73, 75], [75], [104], [84], [102], [88], [88], [105, 107], [101], [51], [54], [85], [70], [100],
           [116], [73, 75], [65], [103, 105], [48], [99, 101], [116], [82], [90], [49, 51], [68], [111], [72], [80], [120, 122], [55], [76, 78], [120], [74], [80], [101, 103], [72], [108]]

traversel(key_arr,'',40,64)

key= "UQ8yjqwAkoVGm7VDdhLoDk0Q75eKKhTfXXke36UFdtKAi0etRZ3DoHPz7NxJPgHl"
key_array= [ord(i) for i in key]
# print(decode_64(key_array))
decode_full(key_array)
