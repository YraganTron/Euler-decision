a = 2520
k = 0
while k == 0:
    a += 1
    for x in range(1,21):
        if a % x == 0:
            k = 1
            continue
        else:
            k = 0
            break
print(a)