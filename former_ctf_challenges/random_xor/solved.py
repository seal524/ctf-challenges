import random as r
encrypted = "QTQ@SPFFS@PBJGG"
t=""
r.seed((500 + 1500)/200 * 6 / 300);
for i in range(len(encrypted)):
        num = r.randint(1,5)
        t += chr(ord(encrypted[i]) ^ num)
print(t)
