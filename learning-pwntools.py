# https://play.picoctf.org/practice/challenge/18
from pwn import *

context.log_file = './learning-pwntools.log'
# context.log_level = 'debug'

io = remote('mercury.picoctf.net', 22342)
io.send('GET /\r\n\r\n')
with context.local(log_level='debug'):
    mylist = io.recv().decode("utf-8").strip().split('\n')
# print(mylist)

characters = [chr(int(n)) for n in mylist]
# print(characters)

flag = ''.join(characters)
print(flag)
info(flag)