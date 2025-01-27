# Linspace-
# numpy.linspace() creates an array of evenly spaced values over a specified interval. You control the number of points directly, rather than the step size.
# Syntax: numpy.linspace(start, stop, num, endpoint=True)

# for example
import numpy as np
a = np.linspace(0, 10)
print(a)
# Output: [ 0.          0.20408163  0.40816327 ...  9.79591837 10.        ]
# default numbers are 50 if numbers are not specified

# to specify number we pass it as an attribute
# to exclude the end point we use endpoint=False
import numpy as np
b = np.linspace(0, 10,10,endpoint=False)
print(b)


# Arange-
# numpy.arange creates an array of evenly spaced values within a specified range. You can control the start, stop, and step size.
# Syntax - numpy.arange(start, stop, step)
# for eg-
c = np.arange(0, 10, 2)
print(c)
# Output: [0 2 4 6 8]

# For negative step size
d = np.arange(10,0,-2)
print(d)
# Output:[10  8  6  4  2]





