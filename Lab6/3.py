import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

N = 1000
lst = np.random.randn(N)

print("\nRaw data:", lst)
lst.sort()
print("Sorted data:", lst)


def get_mean(list):
    return float(sum(list)/len(list))


def get_median(list):
    median_pos = (len(list)+1)/2
    if median_pos == int(median_pos):
        median_pos = int(median_pos-1)
        return list[median_pos]
    else:
        med_avg = []
        med_avg.append(list[int(median_pos-1.5)])
        med_avg.append(list[int(median_pos-.5)])
        return get_mean(med_avg)

def mode(data):
    most = max(set(data), key=data.count)
    print('the mode is: ' , most , '\n')




print("Mean:", get_mean(lst))
print("Median:", get_median(lst))

dpi = 100
fig = plt.figure(dpi=dpi, figsize=(600 / dpi, 400 / dpi))
fig = plt.figure(get_mean(lst))
mpl.rcParams.update({'font.size': 10})

plt.title('hello, my friend. how do you do?')

ax = plt.axes()

xs = range(len(lst))
plt.bar([x + 0.0 for x in xs], lst,
        color='blue', alpha=0.8,
        zorder=0)
plt.xticks(xs, lst, rotation=10)
plt.show()

