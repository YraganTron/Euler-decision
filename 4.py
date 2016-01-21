def palindrom(x):
    b = []
    i = 0
    k = 0
    while x >= 1:
        b.append(x % 10)
        x //= 10
    if len(b) % 2 == 0:
        while i != len(b) / 2:
            if b[i] == b[-i-1]:
                k += 1
            i += 1
        if k == len(b) / 2:
            return True
        else:
            return False
    else:
        while i != (len(b) // 2):
            if b[i] == b[-i-1]:
                k += 1
            i += 1
        if k == len(b) / 2:
            return True
        else:
            return False

w = []
q = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        q = x * y
        if palindrom(q) == True:
            w.append(q)
print(max(w))



