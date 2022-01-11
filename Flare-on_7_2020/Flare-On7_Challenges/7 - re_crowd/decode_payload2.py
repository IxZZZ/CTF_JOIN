from Crypto.Cipher import ARC4

with open('encoded_payload2.bin','rb') as file:
    payload2_encoded = file.read()
    print(hex(len(payload2_encoded)))

    # decode xor
    key = b'KXOR'

    # encoded_1 = []
    # for i in range(len(payload2_encoded)):
    #     k = payload2_encoded[i]^key[i%len(key)]
    #     encoded_1.append(k)
    
    # print(encoded_1[:4])
    # encoded_1_bytes = b''.join(bytes([i]) for i in payload2_encoded[4:])
    key_rc4 = b'killervulture123'
    cipher = ARC4.new(key_rc4)
    payload2_decoded = cipher.decrypt(payload2_encoded[4:])
    with open('payload2_final.bin','wb') as pay:
        pay.write(payload2_decoded)
