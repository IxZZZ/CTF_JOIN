def decode_dll():
    key_xor_dll = [0x8,0x67,0x53,0x9]

    with open('dll_encoded.dll','rb') as file:
        encoded = file.read()
        decoded = b''
        i = 0
        for en in encoded:
            index = i
            i = (i+1)&3
            decoded += bytes([key_xor_dll[index]^en])
        
        with open('dll_decoded.dll','wb') as out:
            out.write(decoded)

def decode_name():
    key_xor_common = b'<g~{<it'
    with open('filename_encoded','rb') as file:
        encoded = file.read()
        i = 0
        for en in encoded:
            print(chr(en^key_xor_common[i%len(key_xor_common)]),end='')
            i += 1
    print()
    with open('namefunc_encoded','rb') as file:
        encoded = file.read()
        i = 0
        for en in encoded:
            print(chr(en^key_xor_common[i%len(key_xor_common)]),end='')
            i += 1
    print('path: ')
    with open('password_encoded','rb') as file:
        encoded = file.read()
        i = 0
        for en in encoded:
            print(chr(en^key_xor_common[i%len(key_xor_common)]),end='')
            i += 1
    
decode_name()

print()
print('done')
