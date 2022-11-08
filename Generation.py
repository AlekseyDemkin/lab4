import random


def gen():
    Al = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    p = ""
    # промежуток
    m = 0
    M = 0
    for i in range(0, 4):
        m += ord(random.choice(Al))
    for i in range(0, 5):
        M += ord(random.choice(Al))

    # генерация ключа
    while True:
        for i in range(0, 13):
            p += random.choice(Al)
        s = p[:5]
        o, q, x = 0, 0, 0
        for y in s:
            o += ord(random.choice(s))
        t = p[5:9]
        for z in t:
            q += ord(random.choice(t))
        r = p[9:13]
        for l in r:
            x += ord(random.choice(r))
        if (m < o < M) or (m < q < M) or (m < x < M):
            break
    return p
