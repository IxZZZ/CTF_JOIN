import string


def sum_shift(a, b):
    return ((a >> 4)+(b << 4)) & 0xff


def mul_2_check(a):
    a = a & 0xFF
    if (a >> 7) == 1:
        a = ((a*2) | 1) & 0xff
    else:
        a = (a*2) & 0xff

    return a


def brutce_force_bytes(b1, b2):
    digits = string.printable
    for i_1 in digits:
        for i_2 in digits:
            sum1 = sum_shift(ord(i_1), ord(i_2))
            sum2 = sum_shift(ord(i_2), ord(i_1))

            cal_1 = mul_2_check(
                (mul_2_check(mul_2_check(sum1)))) ^ 0x13
            cal_2 = mul_2_check(mul_2_check(sum2)) ^ 0x37

            if cal_1 == b1 and cal_2 == b2:
                print(i_1+i_2, end='')
                return


f = open('flag.txt.enc.reserverd', 'rb')

bytes = f.read()

for i in range(0, len(bytes), 2):

    brutce_force_bytes(bytes[i], bytes[i+1])
