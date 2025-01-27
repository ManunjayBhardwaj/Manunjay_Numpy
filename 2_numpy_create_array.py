# Now we will create a numpy ndarray object
# The array object in numpy is called ndarray
# made by array() function
import numpy as np
x = np.array([1,2,3,4,5])# here a list is given
print(x)
print(type(x))# this gives output as <class 'numpy.ndarray'>

# we can also pass a list , tuple or any array like object with array() and it will be converted to ndarray

import numpy as np
y=np.array((1,2,3,4,5))# here the input is tuples
print(y)
print(type(y))# here also the output is ndarray

# Dimensions in array
# a dimension is one level of array depth(nested array)

# 0-D Arrays -scalars, are the elements in an array
# each value in an array is a 0-Dimensional array

# Now we will curate a 0-D array with value 42
import numpy as np
z=np.array(42)
print(z)

# 1-D arrays -an array that has 0-D arrays as its elements is called uni directional or 1-D
import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(a.ndim)
print("\n")

# Create a 2-D array containing 2 arrays with certain values
import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print("\n")

# Now we will create a 3-D array with two  2-D array
# 3-D array is made up from two 2-D arrays
import numpy as np
c=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(c)
print(c.ndim)
print("\n")
# to check how many dimensions are there in an array : ndim attribute

print(a.ndim)
print(b.ndim)
print(c.ndim)
print("\n")

# Create an array with 5-D and verify that it has 5 dimensions
import numpy as np
d=np.array([1,2,3,4,5], ndmin=5)
print(d)
print("The dimension of the array is :",d.ndim)

# Using the ndmin attribute we can assign any dimension to a given array