flag = input("flag: ")

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

scrambled = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]


for i in range(0,len(flag),6):
    scrambled[i+3] = a[(ord(flag[i+3]))%len(a)]

    scrambled[i+4] = a[(ord(flag[i+4]))%len(a)]

    scrambled[i+1] = a[(ord(flag[i+1]))%len(a)]

    scrambled[i+5] = a[(ord(flag[i+5]))%len(a)]

    scrambled[i] = a[(ord(flag[i]))%len(a)]

    scrambled[i+2] = a[(ord(flag[i+2]))%len(a)]


scrambled = ''.join(scrambled)
print(scrambled)