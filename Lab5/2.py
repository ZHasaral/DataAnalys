import numpy as np
N = int(input())
mass = np.ones((N,N))
mass[1:-1,1:-1] = 0
print(mass)
