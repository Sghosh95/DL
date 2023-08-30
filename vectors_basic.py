"""define the shape to know if your matrix is correctly defined or not"""
import numpy as np
a=np.random.randn(5,)
print(a)
print(a.shape) #-->(5,) so this is not a perfectly defined vector

"""transpose"""
print(a.T)
"""dot product"""
print(np.dot(a,a.T))


"""defined a matrix mx1"""

b=np.random.randn(5,1)
print(b)
print(b.shape)

print(b.T)
print(np.dot(b,b.T))