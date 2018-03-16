import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.patches as mpatches


N = 1000
M = 50
lst=np.random.randn(N)
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

def ser(list):
    if (len(list)%2==0):
        l1 = list[0:N//2]
        l2 = list[len(l1):len(list)]
    else:
        l1 = list[0:N // 2]
        l2 = list[len(l1)+1:len(list)]
    return l1,l2


a, b = ser(lst)
print(a,b)
print(get_median(a))
print(get_median(b))


count, bins, ignored = plt.hist(lst, M, normed=True)
plt.axvline(get_median(a), label='Quartile 1', color='r', linestyle='--', linewidth=2)
plt.axvline(get_median(lst), label='Quartile 2',color='y', linestyle='-', linewidth=2)
plt.axvline(get_median(b), label='Quartile 3', color='g', linestyle='--', linewidth=2)


plt.legend(loc='upper right')
plt.show()