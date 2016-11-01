a = 2
b = 2

answer = set()

while a <= 100:
    while b <= 100:
        answer.add(a**b)
        b += 1
    a += 1
    b = 2
print(len(answer))
