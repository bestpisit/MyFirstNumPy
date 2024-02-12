import numpy as np

A = np.array([[1,2],[3,4]])   # 2D array
b = np.array([5,6])           # 1D array

x = np.linalg.solve(A,b)      # ใช้ฟังก์ชัน linalg.solve() ในการหาคำตอบ
print(x)

x = np.linalg.inv(A) @ b      # หาคำตอบโดยคำนวณหาค่าของ A-inverse @ b
print(x)