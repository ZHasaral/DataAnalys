import matplotlib.pyplot as plt
import numpy as np
import statistics as st


N = 1000
M = 40
lst=np.random.randint(1,10,N)
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

print(st.mode(lst))
def get_mean(list):
    return float(sum(list)/len(list))
count, bins, ignored = plt.hist(lst, M, normed=True)
plt.axvline(get_mean(lst), color='b', linestyle='dashed', linewidth=2)
plt.axvline(get_median(lst), color='r', linestyle='-', linewidth=2)
# plt.axvline(st.mode(lst), color='r', linestyle='-', linewidth=2)
plt.show()