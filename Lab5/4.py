import numpy as np
list=[]
mass = np.arange(11)
print(mass)
p = np.random.randint(0,50)
print(p)
r = np.random.randint(0,11)

for i in range(r):
    list.append(mass[i])
list.append(p)

for i in range(r,len(mass)):
     list.append(mass[i])
print(mass)
print(list)

