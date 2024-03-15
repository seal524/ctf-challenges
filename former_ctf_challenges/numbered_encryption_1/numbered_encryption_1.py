import secret

secret = secret.upper()
flag = f"CTFkom{secret}"

encrypted = ""
for i in range(len(secret)):
    encrypted += str(ord(secret[i]))

print(encrypted)
