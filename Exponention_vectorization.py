"""Suppose you need to apply exponential operation on every element of vector/matrix"""

import numpy as np
import math
import time
u=np.zeros((100000,1))
# print(u)

v=np.ones((100000,1))

start=time.time()
for i in range(100000):
    u[i]=math.exp(v[i])
end=time.time()
print(u)
print(str(1000*(end-start)))

"""with using vectorization"""

start_v=time.time()
u=np.exp(v)
end_v=time.time()
print(u)
print(str(1000*(end_v-start_v)))