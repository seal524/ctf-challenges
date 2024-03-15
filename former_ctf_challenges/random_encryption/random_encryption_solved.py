from random import *

flag = "KXAjiv~L0ng-qat07iv"


seed(10)
randomNumbers = []
for i in range(len(flag)*2):
    num = randint(1,13)
    randomNumbers.append(num)

#reversing last step
s = ""
i = 0
for num in randomNumbers[len(flag):]:
    s += chr(ord(flag[i]) - num)
    i += 1

flag = s

#reversing second step
flag = list(flag)
flag.reverse()
flag = "".join(flag)

#reversing step one
s = ""
i = 0
for num in randomNumbers[:len(flag)]:
    s += chr(ord(flag[i]) + num)
    i += 1

flag = s

#reversing start
flag = list(flag)
flag.reverse()
flag = "".join(flag)

#result
print(flag)