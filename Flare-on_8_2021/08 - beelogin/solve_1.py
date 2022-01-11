import base64
from z3 import *

file = open('solve.txt', 'r')

str = file.read()

str_decoded_constant_1 = base64.b64decode(str)

str_decoded_constant_2 = base64.b64decode(
    "b2JDN2luc2tiYXhLOFZaUWRRWTlSeXdJbk9lVWxLcHlrMXJsRnk5NjJaWkQ4SHdGVjhyOENQeFE5dGxUaEd1dGJ5ZDNOYTEzRmZRN1V1emxkZUJQNTN0Umt6WkxjbDdEaU1KVWF1M29LWURzOGxUWFR2YjJqQW1HUmNEU2RRcXdFSERzM0d3emhOaGVIYlE3dm9aeVJTMHdLY2Vhb3YyVGQ4UnQ2SXUwdm1ZbGlVYjA4YVRES2xESnlXU3NtZENMN0J4MnBYdlZET3RUSmlhY2V6Y3B6eUM2Mm4yOWs=")


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
    file = open('decode_js.js','w')
    str_res =  ''.join([chr(i) for i in res])
    file.write(str_res)
    file.close()
    print('Done decode!')


def traversel(arr, str, i, stop):
    if i == stop:
        print(str+'  --> ', decode_64([ord(c)
              for c in "ChVCVYzI1dU9cVg1ukBqO2u4UGr9aVCNWHpMUuYDLm"+str]))
        return
    for o in arr[i]:
        traversel(arr, str+chr(o), i+1, stop)



print(len(str_decoded_constant_1))
print(len(str_decoded_constant_2))

key_arr=[[65, 67], [102, 104], [86], [67], [84, 86], [89], [120, 122], [73], [49], [98, 100], [85], [57], [97, 99], [86], [103], [49, 47], [117], [107], [66], [111, 113], [79], [50], [117], [52], [83, 85], [71], [114], [55, 57], [97, 95], [86], [67], [78], [87], [70, 72], [110, 112], [75, 77], [85], [117],
           [87, 89], [68], [76], [109], [66, 68], [79], [48, 50], [48, 50], [99], [100], [102, 104], [88], [113], [51], [111], [113], [112], [54, 56], [106], [109], [75], [66, 64], [70, 72], [83, 85], [85, 87], [73]]


# traversel(key_arr,'',42,64)

key= "ChVCVYzI1dU9cVg1ukBqO2u4UGr9aVCNWHpMUuYDLmDO22cdhXq3oqp8jmKBHUWI"
key_array= [ord(i) for i in key]
# print(decode_64(key_array))
decode_full(key_array)
