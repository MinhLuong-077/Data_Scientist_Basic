import numpy as np

# Khởi tạo mảng một chiều với kiểu dữ liệu các phần tử là Integer
arr = np.array([1, 3, 4, 5, 6], dtype=int)

# Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
arr = np.array([1, 3, 4, 5, 6])

print(arr)

from random import  randrange
while True:
    x=randrange(-100,100)
    print(x)
    if x==0:
        break
