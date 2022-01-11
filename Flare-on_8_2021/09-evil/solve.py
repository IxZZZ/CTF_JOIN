from pwn import *
import socket
s = socket.socket()

p = remote('127.0.0.1',1226)

p.sendline(p32(10)+ b'A'*10)
