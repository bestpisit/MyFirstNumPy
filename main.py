import numpy as np
import math

# broadcasting error
x1 = np.array([[1,2],[3,4],[5,6]]) # shape (3,2)
x2 = np.array([[1,2,3],[4,5,6]])   # shape (2,3)
print(x1 - x2)