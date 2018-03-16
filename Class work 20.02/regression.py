import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

plt.plot(x,y,fit_fn(x))
plt.xlim(0, 5)
plt.ylim(0, 12)
plt.show()