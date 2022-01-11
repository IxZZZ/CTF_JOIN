import hashlib

str = b"ABCDABCDABCDABCDABCDABCDABCDABC\x00"

print(str.decode())

hash3_512 = hashlib.sha3_512()

hash3_512.update(str)


print(hash3_512.hexdigest())

hash_256 = hashlib.sha256()



hash_256.update(hash3_512.digest())

print(hash_256.hexdigest())
