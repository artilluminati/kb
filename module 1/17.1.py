import numpy as np
from icecream import *

arr = np.random.randint(1, 100, size=(10))
ic(arr)

norm = np.linalg.norm(arr)
norm_arr = arr/norm

ic(norm_arr)