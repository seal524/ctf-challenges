import random as r
import base64

secret_code = open("encrypted_code.txt", "r").read()

def b64(text):
    m = text
    m_b = m.encode('ascii')
    b64_b = base64.b64encode(m_b)
    b64_m = b64_b.decode('ascii')

    return b64_m


def secretXor(text):
    text = text.upper()
    r.seed((500 + 1500)/200 * 6 / 300);
    t = "aaa"
    for i in range(len(text)):
        num = r.randint(1,5)
        t += chr(ord(text[i]) ^ num)
    t += "aaa"
    t = b64(t)
    return t

code = input("Secret code: ") 
code = secretXor(code)

if code == secret_code:
    print("Congrats you solved the challange!")
    flag = open("flag.txt", "r").read()
    print(flag)
