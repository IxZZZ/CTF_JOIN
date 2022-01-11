import pickle


file = open('flag.png.encrypted', 'rb')

str = file.read()

with open('dict_db.pickle', 'rb') as handle:
    dict_db = pickle.load(handle)


out_file = open('flag.png', 'wb')
for i in range(0, len(str), 2):
    byte_decrypt = (str[i+1] << 8) | str[i]
    byte_encrypt = dict_db[byte_decrypt]
    
    out_file.write(bytes([byte_encrypt & 0xff]))
    out_file.write(bytes([byte_encrypt >> 8]))

out_file.close()
