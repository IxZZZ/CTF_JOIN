import base64
import string


def decode(key):

    res = []
    for i in range(64):
        res.append(
            (str_decoded_constant_1[i]-((str_decoded_constant_2[i % 221] + key[i] & 0xff))) & 0xff)
    # print(''.join([chr(i) for i in res]))
    print(res)


def check(str):
    if str.count('(') != str.count(')') or str.count('[') != str.count(']') or str.find('[+]') != -1:
        return False


def traversel(arr, str, i, stop):
    if i == stop:
        if check(str) == False:
            return
        print(str)
        return
    for o in arr[i]:
        traversel(arr, str+chr(o), i+1, stop)


def brute(i):
    arr = []
    for c in string.printable:
        map_arr = [91, 93, 40, 41, 33, 43]
        cal = (str_decoded_constant_1[i] -
               ((str_decoded_constant_2[i % 221]+ord(c)) & 0xff)) & 0xff
        if cal in map_arr:
            arr.append(cal)
    return arr


def check_js(arrs):
    for arr in arrs:
        if len(arr) == 0:
            return False
    return True


file = open('solve_payload2.txt', 'r')

str = file.read()

str_decoded_constant_1 = base64.b64decode(str)

str_decoded_constant_2 = base64.b64decode(
    "N0l2N2l2RTVDYlNUdk5UNGkxR0lCbTExZmI4YnZ4Z0FpeEpia2NGN0xGYUh2N0dubWl2ZFpOWm15c0JMVDFWeHV3ZFpsd2JvdTVSTW1vZndYRGpYdnhrcGJFS0taRnZOMnNJU1haRXlMM2lIWEZtN0RSQThoMG8yYUhjNFZLTGtmOXBDOFR3OUpyT2RwUmFOOUdFck12bXd2dnBzOUVMWVpxRmpnc0ZHTFFtMGV4WW11Wmc1bWRpZWZ6U3FoZUNaOEJiMURCRDJTS1o3SFpNRzcwRndMZ0RCNFFEZWZsSWE4Vg==")

key = ''
count = 0
print(len(str_decoded_constant_1))
print(len(str_decoded_constant_2))

ascii = string.printable
arr_ascii = [ord(i) for i in ascii]
# traversel(arr_res, '', 0, 7)
len_combine = len(str_decoded_constant_1)//len(str_decoded_constant_2)
# len_combine = 1

possible = [[] for i in range(64)]
for i in range(64):
    for c in arr_ascii:
        arr = []
        step = 0
        cnt = 0
        while step < len_combine*(len(str_decoded_constant_2)):
            small_step = 0
            while small_step+i < len(str_decoded_constant_2):
                cnt += 1
                cal = (c+str_decoded_constant_2[i+small_step]) & 0xFF
                cal_1 = (str_decoded_constant_1[step+small_step+i]-cal) & 0xFF
                if cal_1 in arr_ascii:
                    arr.append(cal_1)
                # print(step+small_step+i)
                small_step += 64
            step = step + len(str_decoded_constant_2)

        if len(arr) == cnt:
            s = ''.join([chr(k) for k in arr])
            # print(chr(c),end=' ')
            if '+]' in s:
                # print(chr(c),end=' ')
                possible[i].append(c)


print(possible)

# key = [[85], [79, 81], [56], [121], [104, 106], [111, 113], [117, 119], [65], [107], [111], [86], [69, 71], [109], [55], [86], [66, 68], [100], [104], [76], [111], [68], [107], [48], [81], [55], [53], [101], [73, 75], [75], [104], [84], [102], [88], [88], [105, 107], [101], [51], [54], [85], [70], [100],
# [116], [73, 75], [65], [103, 105], [48], [99, 101], [116], [82], [90], [49, 51], [68], [111], [72], [80], [120, 122], [55], [76, 78], [120], [74], [80], [101, 103], [72], [108]]
