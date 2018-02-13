import random
import numpy as np

heads = int(0)
tails = int(0)
flipCount = int(1000)
while (flipCount > 0):
    flip = random.randint(0,1)
    if flip == 0:
        flipWord = "heads"
        heads += 1
    else:
        flipWord = "tails"
        tails+=1
    print ("I flipped a coin and got ",flipWord,".")
    flipCount -= 1
print(tails,heads)