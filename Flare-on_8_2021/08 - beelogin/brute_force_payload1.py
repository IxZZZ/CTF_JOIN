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


file = open('solve_payload1.txt', 'r')

str = file.read()

str_decoded_constant_1 = base64.b64decode(str)

str_decoded_constant_2 = base64.b64decode(
    "b2JDN2luc2tiYXhLOFZaUWRRWTlSeXdJbk9lVWxLcHlrMXJsRnk5NjJaWkQ4SHdGVjhyOENQeFE5dGxUaEd1dGJ5ZDNOYTEzRmZRN1V1emxkZUJQNTN0Umt6WkxjbDdEaU1KVWF1M29LWURzOGxUWFR2YjJqQW1HUmNEU2RRcXdFSERzM0d3emhOaGVIYlE3dm9aeVJTMHdLY2Vhb3YyVGQ4UnQ2SXUwdm1ZbGlVYjA4YVRES2xESnlXU3NtZENMN0J4MnBYdlZET3RUSmlhY2V6Y3B6eUM2Mm4yOWs=")

key = ''
count = 0
print(len(str_decoded_constant_1))
print(len(str_decoded_constant_2))

ascii = string.printable
arr_ascii = [ord(i) for i in ascii]
# traversel(arr_res, '', 0, 7)
len_combine = 783067//221
# len_combine = 1

possible = [[] for i in range(64)]
for i in range(64):
    for c in arr_ascii:
        arr = []
        step = 0
        cnt = 0
        while step < len_combine*(221):
            small_step = 0
            while small_step+i < len(str_decoded_constant_2):
                cnt += 1
                cal = (c+str_decoded_constant_2[i+small_step]) & 0xFF
                cal_1 = (str_decoded_constant_1[step+small_step+i]-cal) & 0xFF
                if cal_1 in arr_ascii:
                    arr.append(cal_1)
                # print(step+small_step+i)
                small_step += 64
            step = step + 221

        if len(arr) == cnt:
            s = ''.join([chr(k) for k in arr])
            # print(chr(c),end=' ')
            if '+]' in s:
                # print(chr(c),end=' ')
                possible[i].append(c)


print(possible)

key = [[65, 67], [102, 104], [86], [67], [84, 86], [89], [120, 122], [73], [49], [98, 100], [85], [57], [97, 99], [86], [103], [49, 47], [117], [107], [66], [111, 113], [79], [50], [117], [52], [83, 85], [71], [114], [55, 57], [97, 95], [86], [67], [78], [87], [70, 72], [110, 112], [75, 77], [85], [117],
       [87, 89], [68], [76], [109], [66, 68], [79], [48, 50], [48, 50], [99], [100], [102, 104], [88], [113], [51], [111], [113], [112], [54, 56], [106], [109], [75], [66, 64], [70, 72], [83, 85], [85, 87], [73]]
