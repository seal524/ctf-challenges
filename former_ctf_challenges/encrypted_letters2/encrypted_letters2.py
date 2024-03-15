import random
import base64
from inputimeout import inputimeout 

letters="ABCDEFGHIJKLMNOPQRSTUVWZabcdefghijklmnopqrstuvwz123456789"
done = True

for i in range(30):
    secretCode=""
    for i in range(30):
        secretCode += letters[random.randint(1, len(letters))-1]

    def b64(text):
        m = text
        m_b = m.encode('ascii')
        b64_b = base64.b64encode(m_b)
        b64_m = b64_b.decode('ascii')

        return b64_m


    print(f"Secret code: {b64(secretCode)}")
    try: 
        inputCode = inputimeout(prompt=f"Enter the secret code decoded: ", timeout=3) 
        if inputCode == secretCode:
            print("Correct!")
        else:
            done = False
    # Catch the timeout error 
    except Exception: 
       print("Your time is over! Restart the connection.")
       done = False


if done:
    print("Congrats you solved the challenge!")
    flag = open("flag.txt", "r").read()
    print(flag)