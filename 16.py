sum = 0
a = 2**1000
while a >= 1:
    sum += a % 10
    a //= 10
print(sum)