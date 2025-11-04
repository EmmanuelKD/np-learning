import numpy as np

# ar =np.array([[1,2,3],[4,5,6],[3,4,5]])

# print(ar.ndim)

# row , col=ar.shape


# print(row,col)

# arr=np.arange(6,dtype=np.int32)

# ar[0,1]=10
# # c = np.empty((3,3), dtype=np.float32) 

# # arr.reshape(-1)

# vec = np.array([2,4], dtype=np.int32)[:,None]

# print(ar)

# print("====================")
# ar=ar+1
# print(ar)
# print("=======vec=============")
# print(vec)
# c=np.arange(8,10,dtype=np.int32)
# r1= np.random.rand(1,4,3)
# print(r1)
# print(r1.ndim)


# a = np.arange(6, dtype=np.int32).reshape((2,3))
# print("The 2D 'a' array:\n", a)
# print("   ... its shape is", a.shape)

# vec = np.array([2,4], dtype=np.int32)[:,None]
# print("\nThe 'vec' array:\n", vec)
# print("   ... its shape is", vec.shape)


a = np.arange(6, dtype=np.int32).reshape((2,3))
print("The 2D 'a' array:\n", a)
print("   ... its shape is", a.shape)

vec = np.array([2,4], dtype=np.int32)[:,None]
print("\nThe 'vec' array:\n", vec)
print("   ... its shape is", vec.shape)

print("\nAdding:\n", a+vec)
print("\nSubtracting:\n", a-vec)
print("\nMultiplying:\n", a*vec)
print("\nFloat division:\n", a/vec)   # this would be integer div in Python2 since both array are of int type!!!
print("\nInteger division:\n", a//vec)
print("\nPower:\n", a**vec)
print("\nModulo:\n", a%vec)
print("\nElementwise maximum:\n", np.maximum(a, vec))
print("\nEqual:\n", a == vec)
print("\nGreater:\n", a > vec)

print("====================")

a = np.arange(10, dtype=np.int32).reshape((2,5))
b = (a % 3 == 0)    # True for elements divisible by 3
print("The 2D 'b' array:\n", b)
print("   ... its shape is", b.shape)
print("   ... its data type is", b.dtype)  # np.bool_

c = (a % 2 != 0)    # True for elements not divisible by 2 (odd numbers)
for i in range(2):
  for j in range(5):
    c[i,j] = a[i,j] % 2 != 0

print("\nThe 2D 'c' array:\n", c)
print("   ... its shape is", c.shape)
print("   ... its data type is", c.dtype)  # np.bool_

print("\nElementwise logical AND of the two arrays:\n", b & c)  # 'and' (1.2 and 1) => (True and True)
np.logical_and(b, c)
print("\nElementwise logical OR of the two arrays:\n", b | c)
print("\nElementwise logical NOT of array 'b':\n", ~b)