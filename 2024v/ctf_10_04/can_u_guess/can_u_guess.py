flag = input("flag: ")

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
encrypted = ""
keys = [0,1,2,3]

for i in keys:
    keys[i] = ord(flag[i])

for i in range(len(flag)):
    if (i % 4 == 0):
        encrypted += chr(ord(flag[i]) + i)
    elif (i % 4 == 1):
        encrypted += chr(ord(flag[i]) - i)
    elif (i % 4 == 2):
        encrypted += chr(ord(flag[i]) * i)
    elif (i %4 == 3):
        encrypted += chr(ord(flag[i]) + i^2)


for i in encrypted:
    print(ord(i))