a = range(1,101)
sum_1 = 0
sum_2 = 0
for x in a:
    sum_1 += x*x
    sum_2 += x
print(sum_2*sum_2-sum_1)
