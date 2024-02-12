import numpy as np
import math

x = np.array([[1,5,3,1],[0,1,2,9]])

print(x); print()
print(f"np.sum(x): {np.sum(x)}")                    # sum of all axes
print(f"np.sum(x, axis=0): {np.sum(x, axis=0)}")    # column sum
print(f"np.sum(x, axis=1): {np.sum(x, axis=1)}")    # row sum