a = [2, 3, 5, 7, 11, 13]
i = 13
while len(a) != 10001:
    i += 1
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7 or i % 10 == 9:
        for x in a:
            if i % x == 0:
                break
        else:
            a.append(i)
print(a[-1])

















"""
a = [x for x in range(2,1000000)]
b = []
c = []
i = 0
while i != 1:
    if len(a) != 0:
        b.append(a[0])
        a.pop(0)
        for x in a:
            if x % b[-1] != 0:
                c.append(x)
        a.clear()
    else:
        i = 1
    if len(c) != 0:
        b.append(c[0])
        c.pop(0)
        for x in c:
            if x % b[-1] != 0:
                a.append(x)
        c.clear()
    else:
        i = 1
print(a)
print(len(b))
print(c)
"""