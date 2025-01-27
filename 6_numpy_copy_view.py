# Difference between Numpy array copy vs view
# We will make a copy , change in original array, and display both

import numpy as np
a=np.array([1,2,3,4,5])
a1=a.copy()
a1[0]=12
print(a)
print(a1)
# by using the copy function we make a copy of the array 
# and any change in the copy will result to nothing in the original array as it is now a completely independant new array
 
# now we will make a view , change original , display both
import numpy as np
b=np.array([1,2,3,4,5])
b1= b.view()
b[0]=42
print(b)
print(b1)
# now here unlike copy whenever a change is made in the view or the original array it gets reflected in both as view is just a image of the actual array and not a copy
