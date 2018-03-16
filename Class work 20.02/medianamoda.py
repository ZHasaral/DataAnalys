import numpy as np
list = []
for i in range(int(input())):
    list.append(np.random.randint(1,5))
print(list)

def avg(list):
    sum = float(0)
    for i in range(len(list)):
        sum+=list[i]
    print(sum/len(list))

avg(list)
print(sorted(list))

def median(list):
    n = len(list)
    if n % 2 == 1:
            print(sorted(list)[n//2])
    else:
            print(sum(sorted(list)[n//2-1:n//2+1])/2.0)

median(list)

