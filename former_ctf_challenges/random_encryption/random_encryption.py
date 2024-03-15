from random import *

def finalStep(text):
    s = "...........".strip(".")
    for i in range(len(text)):
        num = randint(1,13)
        s += chr(ord(text[i]) + num)
    print("Final step complete")
    flag = s
    return flag

def stepTwo(text):
    text = list(text)
    text.reverse()
    text = "".join(text)
    print("Step two complete")
    flag = finalStep(text)
    return flag

def stepOne(text):
    t = "        ".strip()
    for i in range(len(text)):
        num = randint(1,13)
        t += chr(ord(text[i]) - num)
    print("Step one complete")
    flag = stepTwo(t)
    return flag

def start(input):
    seed(10)
    input = list(input)
    input.reverse()
    input = "".join(input)
    print("Start complete")
    flag = stepOne(input)
    return flag


userInput = input("Flag: ") 

if (len(userInput) == 19):
    flag = start(userInput)
    if (flag == "KXAjiv~L0ng-qat07iv"):
        print("Correct flag!")
        print("You solved my encryption :(")
    else:
        print("Wrong Flag! Try again")
else:
    print("Flag is not the correct size")
