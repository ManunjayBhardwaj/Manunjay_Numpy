#1-D array
# array indexing is the same as accessing an array element
# start with 0
import numpy as np
a=np.array([1,2,3,4,5])
print(a[0])

# we can get the third and fourth element from adding them
import numpy as np
a=np.array([1,2,3,4,5])
print(a[2]+a[3])

# Accessing the 2-D array - it is like rows and columns
import numpy as np
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Second element of the 1st row is :",b[0][1])
print("Fifth element of the 2nd row is :",b[1][4])

# Accessing the 3-D array
import numpy as np
c=np.array([[[1,2,3],[6,7,8]],[[3,1,2],[0,1,4]]])
print(c)
print(c.ndim)
print(c[0][1][0])# this prints 6
print(c[1,1,0])# this prints 0
# we can also access multiple dimesnions using comma this removes the need of multiple square brackets

