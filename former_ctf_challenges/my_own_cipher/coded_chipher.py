message = open("flag.txt", "r").read()

keyword = "nottheflag"
m_encoded = ""
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword_phrase = ""
num_k = 0
for i in range(len(message)):
    if not message[i] in abc:
        keyword_phrase += message[i]
    else:
        keyword_phrase += keyword[num_k]
        num_k += 1
        num_k = num_k % len(keyword)
for i in range(len(message)):
    if not message[i] in abc:
        m_encoded += message[i]
    else:
        index = abc.index(message[i]) + abc.index(keyword_phrase[i])
        index = index % len(abc)
        m_encoded += abc[index]

print(m_encoded)


