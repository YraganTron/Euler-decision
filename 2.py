fs = [1,2]
s = 0
while fs[-1] + fs[-2] < 4000000:
	fs.append(fs[-1] + fs[-2])

for n in fs:
	if n%2 == 0:
		s += n

print (s)





