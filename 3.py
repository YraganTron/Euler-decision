a = 600851475143
i = 2
q = []
while i != int(600851475143**0.5):
    if a % i == 0:
        a /= i
        q.append(i)
    i += 1
print(q)




