triangle = 0
k = 1
n = 1
a = []
q = 0
while q == 0:
    triangle += k
    while n <= int((triangle**0.5) + 1):
        if triangle % n == 0:
            a.append(n)
            a.append(triangle / n)
        n += 1 
    if len(a) + 1 > 500:
        q = 1
    else:
        a.clear()
    n = 1
    k += 1

print(triangle)    
