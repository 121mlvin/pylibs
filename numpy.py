import numpy as np

a = np.array([1, 2, 3])

b = np.array([2, 3, 4], dtype='int16')

c = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

d = np.array([[9, 8, 7, 8, 9, 10, 11, 12],
              [6, 5, 4, 3, 2, 1, 2, 3]])

print(a * b)  # a*b will not work with default array
print(a.ndim)  # 1
print(c.ndim)  # 2
print(c.shape)  # (2,3)
print(a.dtype)  # int32
print(b.dtype)  # int16
print(a.itemsize)  # 4 bytes
print(b.itemsize)  # 2 bytes
print(d.shape)
print(d[1, 5])  # to get a specific element from second row, fifth column
print(d[0, :])  # to get a specific row
print(d[:, 2])  # to get a specific column
print(d[0, 1:6:2])  # [startindex:endindex:stepsize] getting each second number in range from 1 to 6 with a step 2
print(np.zeros((2, 3, 3)))  # all 0s matrix
print(np.ones((2, 3, 3), dtype='int32'))  # all 1s matrix
print(np.full((2, 3, 3), 21))  # fill with any other num
print(np.full_like(a, 21))  # fill with any other already built shape
print(np.random.rand(4, 2))  # random numbers from 0 to 1
print(np.random.randint(-5, 7, size=(5, 5)))  # random integer numbers from -5 to 6

# making this type of matrix [1 1 1 1 1]
#                            [1 0 0 0 1]
#                            [1 0 9 0 1]
#                            [1 0 0 0 1]
#                            [1 1 1 1 1]
one = np.ones((5, 5), dtype='int32')
zero = np.zeros((3, 3))
zero[1, 1] = 9
one[1:-1, 1:-1] = zero
print(one)

print(a + 2)  #
print(a - 2)  #
print(a / 2)  # mathematics
print(a * 2)  #
