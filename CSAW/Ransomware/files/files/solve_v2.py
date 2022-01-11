file_en = open(
    './2020_IC3Report.pdf', 'rb').read()

file_plain = open(
    './cad0b75505847a4792a67bb33ece21ec9c7bd21395ca6b158095d92772e01637.pdf.cryptastic', 'rb').read()

str_xor = []


for i in range(len(file_en)):
    str_xor.append(file_en[i] ^ file_plain[i])

file_flag = open(
    './ea6b505ffded681a256232ed214d4c3b410c8b4f052775eb7e67dcbd5af64e63.pdf.cryptastic', 'rb').read()


file_out = open('./output.txt', 'wb')


for i in range(len(file_flag)):
    file_out.write(bytes([file_flag[i] ^ str_xor[i]]))

file_out.close()
