import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-4, 4, 0.01)
y = [i**2  for i in x]
plt.plot(x, y, 'b')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Draw line')
plt.show()