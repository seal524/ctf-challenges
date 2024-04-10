output = "FWItxv9Vl00vkuzzzzmhzzzzzzpp1B"

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

scrambled = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

print(len(a))

for i in range(0,len(output),6):
    scrambled[i+3] = (a.index(output[i+3]))
    scrambled[i+4] = (a.index(output[i+4]))
    scrambled[i+1] = (a.index(output[i+1]))
    scrambled[i+5] = (a.index(output[i+5]))
    scrambled[i] =   (a.index(output[i]))
    scrambled[i+2] = (a.index(output[i+2]))

#komenter ut for å få tak i tallene til flagget
for i in range(len(scrambled)):
    scrambled[i]+=62

for i in range(len(scrambled)):
    scrambled[i] = chr(scrambled[i])
    

scrambled = ''.join(scrambled)
print(scrambled)

#CTFkom{Scrrmblqqqqd_qqqqqqggs? 
#♣-1/=§  %44/$.3333&!333333))5☺

#CTFkom{Scr4mbl3333d_444444ggs}