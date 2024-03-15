# This is a bruteforce challange
secret_pin = open("pin.txt", "r").read()

pin = input("Pincode: ")

if len(pin) == 4:
    if pin == secret_pin:
        print("Congrats you solved the challange!")
        flag = open("flag.txt", "r").read()
        print(flag)
    