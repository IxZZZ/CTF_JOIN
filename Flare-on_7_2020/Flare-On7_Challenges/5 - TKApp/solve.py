from Crypto.Cipher import AES
import hashlib,base64
def solve_password_entry():
    arr = [62,
           38,
           63,
           63,
           54,
           39,
           59,
           50,
           39]
    return ''.join([chr(x ^ 83) for x in arr])


Password = solve_password_entry()

Note = "keep steaks for dinner"
Step = "magic"
Desc = "water"

key_arr = [Desc[2],
           Password[6],
           Password[4],
           Note[4],
           Note[0],
           Note[17],
           Note[18],
           Note[16],
           Note[11],
           Note[13],
           Note[12],
           Note[15],
           Step[4],
           Password[6],
           Desc[1],
           Password[2],
           Password[2],
           Password[4],
           Note[18],
           Step[2],
           Password[4],
           Note[5],
           Note[4],
           Desc[0],
           Desc[3],
           Note[15],
           Note[8],
           Desc[4],
           Desc[3],
           Note[4],
           Step[2],
           Note[13],
           Note[18],
           Note[18],
           Note[8],
           Note[4],
           Password[0],
           Password[7],
           Note[0],
           Password[4],
           Note[11],
           Password[6],
           Password[4],
           Desc[4],
           Desc[3]]

key =  ''.join(key_arr).encode()


iv = b'NoSaltOfTheEarth'

print('key: ',key)
print('iv: ',iv)

sha256 = hashlib.sha256()
sha256.update(key)

key_final = sha256.hexdigest()



cipher = AES.new(bytes.fromhex(key_final),AES.MODE_CBC,iv)

f = open('runtime.dll','rb')

out = cipher.decrypt(f.read())

file = open('final.jpg','wb')

file.write(base64.b64decode(out))

