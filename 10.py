a = [2, 3, 5, 7, 11, 13]
i = 13
x = 0
while a[-1] < 2000000:
    i += 1
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7 or i % 10 == 9:
        while a[x] <= int(i**0.5):
            x += 1
            if i % a[x] == 0:
                break
        else:
            a.append(i)
        x = 0
print(sum(a[:-1]))