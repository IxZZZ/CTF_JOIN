file = open('out_6', 'rb')

str = file.read()

file_new = open('encrypt_out_p6', 'wb')
m = 'meoow'
for i in range(len(str)):
    file_new.write(bytes([str[i] ^ ord(m[i % 5])]))

file_new.close()
file.close()
