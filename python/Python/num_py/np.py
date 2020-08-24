import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
# print(dir(arr))
# print(arr)
# print(arr.dtype)

zeros = np.zeros((2, 3))
# print(zeros)

full = np.full((3, 3), 6+10j, dtype=complex)
# print(full)

rndm = np.random.random((2, 2))
# print(rndm)

arng = np.arange(0, 30, 5)
# print(arng)

lspc = np.linspace(0, 10, 10)
# print(lspc)

# rsp = arr.reshape(3, 2, 1)
rsp = arr.reshape(3, 2)
# print(rsp)

# print(arr)
temp = arr[:1, ::2]
# print(temp)

cond = arr>2
t_arr = arr[cond]
# print(t_arr)

mx = arr.max()
# print(mx)

# print(arr)
print(arr)
a_mx = arr.max(axis=0)
# print(a_mx)

c_sum = arr.cumsum(axis=1)
print(c_sum)
