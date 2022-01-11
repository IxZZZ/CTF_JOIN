
str = 'abcdefghijklmnopqrstuvwxyz'

enc = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'.lower()

cipher = 'jmodtrr_tdwumtu_cydy_ynsldf'
for i in cipher:
    j = enc.find(i)
    if j == -1:
        print(i, end='')
    else:
        print(str[j], end='')
