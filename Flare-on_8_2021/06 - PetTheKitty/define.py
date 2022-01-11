from revenge import Process


def xor(filename, i):
    file = open(filename, 'rb')
    content = file.read()

    file_new = open('.\\final_decrypt'+f'\decrypt_{i}.txt', 'wb')
    m = 'meoow'
    for i in range(len(content)):
        file_new.write(bytes([content[i] ^ ord(m[i % 5])]))

    file_new.close()
    file.close()


p = Process(r"C:\Windows\System32\calc.exe")
p.memory['LoadLibraryA'](r"C:\Windows\System32\msdelta.dll")
ApplyDeltaA = p.memory["ApplyDeltaA"]
file = open('communicate', 'rb')
str = file.read()
file.close()


str_s = str.split(b'ME0W')
str_s = str_s[1:]

path_pre = ".\source_pre_xor"
path_after = ".\source_decrypted"
for i in range(0, len(str_s), 2):
    file_name_1 = path_pre + f'\patch_file_{i}'
    file_name_2 = path_pre + f'\src_patch_file_{i}'
    file_1 = open(file_name_1, 'wb')
    file_2 = open(file_name_2, 'wb')
    file_1.write(str_s[i][8:])
    file_2.write(str_s[i+1][8:])
    file_1.close()
    file_2.close()
    print(i)

    check = ApplyDeltaA(1, file_name_2,
                        file_name_1, path_after+f'\out_{i}.txt')
    if check == 0:
        check = ApplyDeltaA(1, file_name_1,
                            file_name_2, path_after+f'\out_{i}.txt')
        if check == 0:
            print('something wrong')
            continue
    # xor(path_after+f'\out_{i}', i)
