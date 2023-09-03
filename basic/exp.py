import numpy as np
x=np.array([[[1],[2]],[[3],[4]]])
print(x.shape)


#import numpy as np
a=np.random.randn(4,3)
b=np.random.randn(4,1)
c=a*b
print(c.shape)


a=np.random.randn(4,3)
b=np.random.randn(4,1)
c=0
for i in range(3):
    for j in range(4):
        c[i][j]=b[j][i]+b[j]
print(c[i][j])