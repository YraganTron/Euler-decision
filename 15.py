a =[[0] * 21 for x in range(21)]
for x in range(len(a)):
    for i in range(len(a[x])):
        if x == 0:
            a[x][i] = 1
            continue
        if i == 0:
            a[x][i] = 1
            continue
        a[x][i] = a[x-1][i] + a[x][i-1]


for x in range(len(a)):
    for i in range(len(a[x])):
        print(a[x][i], end = " ")
    print()

print(a[20][20])
