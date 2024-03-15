from pwn import *
import base64

p = remote('10.212.172.46', 524)
context.log_level = "DEBUG"

def b64(text):
    m = text
    print(m)
    b64_b = base64.decodebytes(m)
    b64_m = b64_b.decode('ascii')
    return b64_b

p.recvuntil("Secret code: ")
secretCode = (p.recvline(keepends=False))
p.recvuntil("Enter the secret code decoded: ")
p.sendline(b64(secretCode))

p.clean()