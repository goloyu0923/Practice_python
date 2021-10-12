# create array
import numpy as np
A = np.array([4, 5, 6])
B = np.array((1, 2, 3))
print(np.zeros(6))
print(np.ones(10))

print(A)
print(B)
print(type(A))
print(type(B))

A[0]=14
print(A)

# mask function
import numpy as np
array_1 = np.array([1, 2, 3])

print(array_1[0])
print(array_1[1:3])
mask = (array_1 % 3 == 0)
print(array_1[mask])

# array's operation
import numpy as np

# one diminsional array
A = np.array([2, 4, 6])
B = np.array([4, 5, 6])
result_1 = A + B
result_2 = A - B
result_3 = A * B
result_4 = A / B

print(result_1)
print(result_2)
print(result_3)
print(result_4)

# two diminsional array
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])

result_1 = A + B

result_1 = A + B
result_2 = A - B
result_3 = A * B
result_4 = A / B

print(result_1)
print(result_2)
print(result_3)
print(result_4)

# transposed matrix
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T)

# dot product
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
C = np.array([[7, 8, 9], [1, 2, 3], [1, 2, 3]])

result_5 = A.dot(C)
print(result_5)

# inner
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [1, 2, 3]])
result_6 = np.inner(A, B)
print(result_6)

# outer
result_7 = np.outer(A, B)
print(result_7)

