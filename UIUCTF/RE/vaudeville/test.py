from pwn import *

p = remote('vaudeville.chal.uiuc.tf', 1337)

p.recvuntil('Challenge:')


number = p.recvline().strip()

print(int(number,10))
