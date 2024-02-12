import numpy as np

x = np.array([[ 1, 10, 1, 3, 5],
            [ 1, 15, 2, 3, 5],
            [ 0, 20, 3, 3, 5],
            [ 1, 25, 4, 3, 5]])

y = (x[:,0] == 1)

print(np.sum(x[y][:,[2,4]],axis=1))