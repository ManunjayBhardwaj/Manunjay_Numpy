# shape of an array - the shape of an array is the number of elements in each dimensions
# now we will try to get the shape of an array
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)
# this shows that this 2-D array has 2 rows and 4 columns
# this also means that the variable has 2 dimensions and each dimension has 4 elements

# now we will create a 5-D array using ndmin
import numpy as np
b=np.array([1,2,3,4],ndmin=5)
print(b.shape)
# the output is (1, 1, 1, 1, 4) 
# we understand that the output of the 5th dimension is 4 as it has 4 elements
# the rest dimensions will give output as 1 as in each dimension a single value is being passed inevidently
