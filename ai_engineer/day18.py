import numpy as np
a=np.array([1,2,3])
print(a)
b=np.asarray(a,dtype=float,order='C')
for i in np.nditer(b):
    print(i)
np.add(a,b,out=b)
print("After addition:", b)