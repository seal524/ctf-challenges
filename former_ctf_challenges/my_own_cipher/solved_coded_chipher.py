def decoder_v(message,keyword):
    m_decoded = ""
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
            m_decoded += message[i]
        else:
            index = abc.index(message[i]) - abc.index(keyword_phrase[i])
            m_decoded += abc[index]
    return m_decoded

