import numpy as np
from icecream import *

arr1 = np.arange(0, 10, 1)

arr1_values ={
    'mean': np.mean(arr1),
    'max': np.max(arr1),
    'min': np.min(arr1)
}

rand1 = np.random.randint(1, 100, (2, 2))
rand2 = np.random.randint(1, 100, (2, 2))

rand_prod = np.matmul(rand1, rand2)

ic(arr1)
ic(arr1_values)
ic(rand1)
ic(rand2)

ic(rand_prod)