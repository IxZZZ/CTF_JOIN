str = "aaaaaa"
str = list(str)
str[1] = '1' 
str[0] =chr(ord('x') ^ 52)
str[2] = chr(50 ^ ord('|'))
str[3] = chr(0x88^0xDD)
str[4] = 'X' 
str[5] = chr(0)
str = "".join(str);
print(str)