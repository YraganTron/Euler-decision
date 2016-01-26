triplet = []
a = 1
b = 1
sum = 0

while b < 1000:
    while a + b + (a**2 + b**2)**0.5 <= 1000:
        if (a**2 + b**2)**0.5 == int((a**2 + b**2)**0.5):
            triplet.append((a, b, (a**2 + b**2)**0.5))
        a += 1
    b += 1
    a = b

for x in range(len(triplet)):
    for y in triplet[x]:
        sum += y
        #print(sum)
    if sum == 1000:
        print(triplet[x])
        sum = 1
        for i in triplet[x]:
            sum *= i
        print(sum)
    sum = 0
