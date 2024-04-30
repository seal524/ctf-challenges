flag = open("output.txt", "rt", encoding="utf-8").read()

hexer = flag.split("0x")

output = ""
num = 0x0

for i in range(len(hexer)):
    if (i != 0):
        #hexer[i] = "0x" + hexer[i]
        output += chr(int(hexer[i], 16) ^ i-1)

print(output)