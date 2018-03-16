import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mass = []
for i in range(int(input())):
    mass.append(np.random.randint(-5,10))
print(mass)
print(mass)

hits = []
for item in mass:
    tally = mass.count(item)
    values = (tally, item)
    if values not in hits:
        hits.append(values)
hits.sort(reverse=True)
if hits[0][0]>hits[1][0]:
    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode")

def avg(list):
    sum = float(0)
    for i in range(len(list)):
        sum+=list[i]
    print(sum/len(list))

avg(mass)

def median(list):
    n = len(list)
    if n % 2 == 1:
            print(sorted(list)[n//2])
    else:
            print(sum(sorted(list)[n//2-1:n//2+1])/2.0)

median(mass)

dpi = 100
fig = plt.figure(dpi = dpi, figsize = (600 / dpi, 400 / dpi) )
fig = plt.figure(median(list))
mpl.rcParams.update({'font.size': 10})

plt.title('hello, my friend. how do you do?')

ax = plt.axes()

xs = range(len(mass))
plt.bar([x + 0.0 for x in xs],  mass,
          color = 'blue', alpha = 0.8,
         zorder = 0)
plt.xticks(xs, mass, rotation =10)
plt.show()
    
      
      
