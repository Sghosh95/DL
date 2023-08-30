import numpy as np
import time
a=np.array([1,2,3,4])
print(a)


#Vectorized version time check
#calculate a dot product

a=np.random.rand(1000000)
b=np.random.rand(1000000)
#start time
start_time=time.time()
c=np.dot(a,b)
#end time
end_time=time.time()
print("Dot product:",c)
print("Vectorized calculation time:" + str(1000*(end_time-start_time))+ "ms" )


#Time check with a for loop
c=0
start_time=time.time()
for i in range(1000000):
    c+=a[i]*b[i]
end_time=time.time()
print("Value calculated of C by for loop :",c)
print("For loop calculation time:" + str(1000*(end_time-start_time))+ " ms")

