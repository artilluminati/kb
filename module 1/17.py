import numpy as np
from icecream import *

arr = np.random.randint(100, size=(100))
ic(arr)

num = int(input('Введите число: '))

new_arr = arr[arr<num]

ic(new_arr)

