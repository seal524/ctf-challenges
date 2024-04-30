flag = open("flag.txt", "rt", encoding="utf-8").read()

output = ""

for i in range(len(flag)):
    output += hex(ord(flag[i]) ^ i)

print(output)

text = open("output.txt", "w", encoding="utf-8").write(output)

