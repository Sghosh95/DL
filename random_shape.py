import numpy as np
a=np.random.randn(1,3)
b=np.random.randn(3,3)


print(a)
print(b)

print((a*b).shape)


c=np.random.randn(1,8)
print(c)
d=np.random.randn(8,8)
print(d)
print((c*d).shape)


a=np.array([[2,1],[1,3]])
print(a)
print(a*a)



a=np.array([[1,1],[1,-1]])
b=np.array([[2],[3]])
c=a+b
print(c)