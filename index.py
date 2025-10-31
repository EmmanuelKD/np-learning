import numpy as np

ar =np.array([[1,2,3],[4,5,6],[3,4,5]])

print(ar.ndim)

row , col=ar.shape


print(row,col)

arr=np.arange(6,dtype=np.int32)

ar[0,1]=10

arr.reshape(-1)

print(arr.ndim)