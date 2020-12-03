def KSA(key, n=256):
    s_temp = [i for i in range(0, n)]
    j = 0
    for i in range(0, n):
        j = (j + s_temp[i] + key[i % len(key)]) % n
        tmp = s_temp[i]
        s_temp[i] = s_temp[j]
        s_temp[j] = tmp
    return s_temp


def PRGA(s, out_len, n=256):
    j = 0
    i = 0
    counter = 0
    k = []
    while counter != out_len:
        i = (i + 1) % n
        j = (j + s[i]) % n
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        k.append(s[(s[i] + s[j]) % n])
        counter += 1
    return k
