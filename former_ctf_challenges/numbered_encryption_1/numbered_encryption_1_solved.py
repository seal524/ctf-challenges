text = "78857766518251689576518484518283"

decrypted = []
for i in range(0,len(text),2):
    decrypted.append(f"{text[i]}{text[i+1]}")

flag = ""
for i in range(len(decrypted)):
    print
    flag += chr(int(decrypted[i]))


a = "{"
b = "}"
print("CTFkom{"+flag+"}")