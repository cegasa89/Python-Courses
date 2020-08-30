import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(x)

y = np.array(x)

print(y)

print()

x = [[[1, 2, 3],[1, 2, 3],[1, 2, 3]],[[1, 2, 3],[1, 2, 3],[1, 2, 3]],[[1, 2, 3],[1, 2, 3],[1, 2, 3]]]

print(x)

y = np.array(x)

print(y)

print()

x = [1, 2, 3, 4, 5]

y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating array object
y = np.array(y)

print(y)

# Creating a 3X3 array with all zeros, +- initialize value
print(np.zeros((3,3)) * 5) 

# Creating a 3X3 array with all ones
print(np.ones((3,4)))

# Creating an array with ones on the diagonal and zeros elsewhere, identity matrix
print(np.eye(4))

# Creating a n array
print(np.arange(100).reshape(10,10))

# Creating an array to n-m with x values
print(np.linspace(0, 100, 5))

# Get Max value in array
print(y.max())

# Get Min value in array
print(y.min())

# Creating a n array with random values
print(np.random.randn(5))

print()

x = np.arange(0,20)

print(x)

print(x[5])

print(x[:10])

print(x[10:])

print(x[-10:-1])

y = x[5:15] = 20

print(y)

print(x)

y = x.copy()

print(y)

print()

x = np.arange(25).reshape(5, 5)

print(x)

print(x[4][3])

print(x[1:4, 1:4])

print()

x = np.arange(10)

print(x)

y = np.arange(10, 20)

print(y)

z = x + y

print(z)

z = x / y

print(z)

print(np.sin(x))

print(np.log(x))

x = np.arange(12).reshape(3, 4)

print(x)

y = np.arange(10, 22).reshape(3, 4)

print(y)

z = x * y

print(z)

print(np.full((2, 2), True))

arr = np.array([0,1,2,3,4,5,6,7,8,9])

x = arr[arr%2==1]

print(x)

a = np.array([1,1,2,3,4,5,6])

b = np.array([0,2,1,3,4,8,9])

print(np.intersect1d(a, b))











