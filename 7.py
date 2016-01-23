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