# Reshaping - means changing the shape of an array, like adding or removing elements

# reshaping from 1-D to 2-D
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a1=a.reshape(4,3)
a2=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# this function means that we will have 4 different arrays each having 3 elements
print(a1)
print(a2)
# both a1 and a2 will give the same output


# reshaping from  1-D to 3-D
import numpy as np
b=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b1=b.reshape(2,2,3)
#this means that the 1-D array will be broken into 2 parts making them 2 2-D arrays and these 2-D arrays will have 2 arrays each and each array will have 3 elements
print(b1)

# the multiplication of all the paramters of the reshape attribute should always be equal to the total number of elements in the array

# Return copy or view
import numpy as np
c=np.array([1,2,3,4,5,6,7,8])
print(c.reshape(2,4).base)
# this gives output as [1 2 3 4 5 6 7 8] 
# as the reshape attribute does not give a distributed 2-D array therefor it is a view
# it is a view because it gives the original value of the array


# Using unknown dimensions - you are only allowed to have one unknown dimension. pass -1
import numpy as np
d=np.array([1,2,3,4,5,6,7,8])
d1=d.reshape(2,2,-1)
print(d1)
# here we just know that we want to divide it into two arrays and each array should have 2 subarrays the number of elements we dont know 
# the -1 here calculates the number of elements in each sub array on its own
# and gives output as [[[1 2][3 4]][[5 6][7 8]]]

# Flattening the array by converting the multidimensional array into 1-D
import numpy as np
e=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
e1=e.reshape(-1)
print(e1)
# passing -1 in the reshape attribute directly converts any dimensional array to a 1-D array


# there a lot of functions for changing the shapes of an array in numpy, like flatten, ravel and
#  also rearranging the element rot90, flip,flipr,flipud. They all come under advanced numpy
