import numpy as np

# Array Creation Methods
# 1. Conversion from other Python structures (eg: list, tuple)
listArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(listArray)
print(listArray.dtype)
print(listArray.shape)
print(listArray.size)

# 2. Intrinsic numpy array creation object
zeros23 = np.zeros((2, 3))
print(zeros23)
print(zeros23.dtype)
print(zeros23.shape)
print(zeros23.size)

rng = np.arange(15)
print(rng)
print(rng.shape)
print(rng.dtype)
print(rng.size)

lin_space = np.linspace(0, 30, 3)  # start, end, number of elements (equally spaced)
print(lin_space)
print(lin_space.dtype)
print(lin_space.size)
print(lin_space.shape)

emp = np.empty((4, 6))  # gives random number array of shape tuple
print(emp)

emp_like = np.empty_like(lin_space)  # gives random number array of size, shape as lin_space
print(emp_like)

ide = np.identity(3)  # give an identity matrix of n=3
print(ide)

print(rng.reshape((3, 5)))  # returns copy of reshaped array, does not reshape the original

# Numpy Axis
x = [[1, 2, 3], [4, 5, 6], [7, 1, 0]]
arr = np.array(x)
print(arr.sum(axis=1))
print(arr.T)  # transpose

for item in arr.flat:
    print(item)

print(f"\n{arr.ndim}")  # dimensions
print(arr.size)
print(arr.nbytes)  # total bytes consumed
print(arr.argmin(axis=0))
print(arr.argmax(axis=0))
print(arr.argsort(axis=0))

one = np.array([4, 0, 4, 2, 1, 2, 3, 0])
print(one.argmax())  # index of max (first occurrence) in array
print(one.argmin())  # index of min (first occurrence) in array
print(one.argsort())  # rearranged index of this array after sort
print(np.array([1, 2, 3]) * np.array([1, 2, 3]))
print(np.array([1, 2, 3]) + np.array([1, 2, 3]))
print(np.array([1, 2, 3]) - np.array([1, 2, 3]))
print(np.sqrt(np.array([1, 4, 9])))

print(np.where(one >= 2))  # returns array of indices that satisfy the given condition
print(np.count_nonzero(one))  # returns the number of non-zeroes in the given array
