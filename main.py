import numpy as np
print(np.__version__)

x1 = np.array([1,2,3,4,5,6])                      # 1D array
x2 = np.array([[1,2,3],[11,22,33],[10,20,30]])    # 2D array

print('---Print numpy arrays:---')
print(f"x1 1D-array: \n{x1}")
print(f"x2 2D-array: \n{x2}")

print('\n------Print 2D list------')
y =[[1,2,3],[11,22,33],[10,20,30]]
print(f"y 2D-List: \n{y}")

print(x1.shape,x1.dtype)
print(x2.shape,x2.dtype)