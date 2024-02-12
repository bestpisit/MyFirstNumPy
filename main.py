import numpy as np
import math

# assign values
x = np.array([
    [ 5, 6, 7, 8],
	  [ 9,10,11,12],
	  [13,14,15,16]])

print(x); print()
x[:,2:] = 0
print(x)