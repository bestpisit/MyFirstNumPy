import numpy as np
import math

x = np.arange(0,360,45)
x = x * np.pi / 180
y = np.sin(x)

print(x)
print(y)