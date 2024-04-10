flag = [67,83,140,108,115,104,738,92,56,78,950,134,60,104,1330,116,133,34,2070,132,71,79,2090,120,135,89,2964,76,127,87,990,158]

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
decrypted = ""
keys = [ord("C"),ord("T"),ord("F"),ord("k")]

for i in range(len(flag)):
    if (i % 4 == 0):
        decrypted += chr(flag[i] - i)
    elif (i % 4 == 1):
        decrypted += chr(flag[i] + i)
    elif (i % 4 == 2):
        decrypted += chr(int(flag[i] / i))
    elif (i %4 == 3):
        decrypted += chr(flag[i] - i^2)


print(decrypted)