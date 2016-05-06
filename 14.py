n = 3
N = n
k = 0
max = [0, 0]
while n <= 10**6:
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3*N + 1
        k += 1
    if k > max[0]:
        max[0] = k
        max[1] = n
    k = 0
    n += 2
    N = n
print(max)

