import sys
a = []

def swap(m,x,y):
    a[x].insert(y,m)
    a[x].pop(y+1)

def max_v(x,y,v):
    if x == 0:
        return v
    else:
        if x == 1:
            return v + a[0][0]
        else:
            if y == 0:
                return v + a[x-1][y]
            elif y == len(a[x]) -1:
                return v + a[x-1][y-1]
            else:
                return v + max(a[x-1][y], a[x-1][y-1])

for line in sys.stdin:
    line = line.rsplit()
    for x in range(len(line)):
        line[x] = int(line[x])
    a.append(line)

for x in range(len(a)):
    for y in range(len(a[x])):
        m = max_v(x,y,a[x][y])
        swap(m,x,y)
print(max(a[-1]))
