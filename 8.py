def multiply(x):
    sum = 1
    for y in x:
        sum *= y
    return sum

a = int(input())
i = int(input())
k = 0
sum = []
max_sum = 0

while a >= 1:
    while k != i and a >= 1:
        k += 1
        if a % 10 != 0:
            sum.append(a % 10)
            a //= 10
        else:
            k = 0
            sum.clear()
            a //= 10
    if len(sum) == 13:
        if multiply(sum) > max_sum:
            max_sum = multiply(sum)
        if a % 10 != 0:
            sum.pop(0)
            sum.append(a % 10)
            a //= 10
        else:
            k = 0
            a //= 10
            sum.clear()
    else:
        break
print(max_sum)
