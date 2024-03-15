flag = input("flag: ") 


def check(flag):
    if ("CTFkom{" in flag and "}" in flag):
        #f
        a = 38 + ord(flag[7])
        #l
        b = 25 - ord(flag[8])
        #a
        c = 55 + ord(flag[9])
        #g
        d = 46 - ord(flag[10])
        #    
        e = 13 + ord(flag[11])
        #c
        if (a+b+c+d+e) != 341:
            return False
        #h
        if (23*a - 16*b -c*(235-55) + (e-512)) != -27403:
            return False
        #e
        if (c*b*23 +a*(-24) + d*e)  != -111695:
            return False
        #c
        if (a + 2354*c - 720*b +4*(e* 50 + d)) != 437217:
            return False
        #k
        if (387*a + 400 -b*2 + e +d*c*5) != 35189:
            return False
        #did u make it here?
        return True
    else:
        return False
    
if check(flag):
    print("Correct flag :)")
else:
    print("Wrong flag :(")

