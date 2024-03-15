import secret

secret = secret.upper()
flag = f"CTFkom{secret}"

def numberCode(text, num):
    if num == 0: 
        text = text.replace("0", "6357")
    elif num == 1:
        text = text.replace("1", "1768")
    elif num == 2:
        text = text.replace("2", "3048")
    elif num == 3:
        text = text.replace("3", "1416")
    elif num == 4:
        text = text.replace("4", "6655")
    elif num == 5:
        text = text.replace("5", "5946")
    elif num == 6:
        text = text.replace("6", "9484")
    elif num == 7:
        text = text.replace("7", "5056")
    elif num == 8:
        text = text.replace("8", "4050")
    elif num == 9:
        text = text.replace("9", "3425")

    return text
    

encrypted = ""
for i in range(len(secret)):
    encrypted += str(ord(secret[i]))

for i in range(0,10):
    encrypted = numberCode(encrypted, i)

print(encrypted)


