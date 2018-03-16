import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.patches as mpatches


N = 1000
M = 40
lst=np.random.randn(N)
print("\nRaw data:", lst)
lst.sort()
print("Sorted data:", lst)

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

def get_mean(list):
    return float(sum(list)/len(list))
print(stats.mode(lst))
mode = stats.mode(lst)
print(get_mean(lst))
print(get_median(lst))
print(mode.mode[0])
fig, ax = plt.subplots(1)

count, bins, ignored = plt.hist(lst, M, normed=True)
plt.axvline(get_mean(lst), label='Mean', color='g', linestyle='--', linewidth=2)
plt.axvline(get_median(lst), label='Median',color='r', linestyle='-', linewidth=1)
plt.axvline(mode.mode[0], label='Mode', color='y', linestyle='-', linewidth=2)

plt.legend(loc='upper right')
plt.show()