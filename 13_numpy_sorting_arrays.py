# Sorting an array
# uses sort() function 

import numpy as np
a=np.array([1,5,2,5,8,2,5,7,3,14,6,0])
print(np.sort(a))# this does not save any value to a new variable and there is no change in the original array as it is a copy not a view
# output :[ 0  1  2  2  3  5  5  5  6  7  8 14]
print(a) #output :[ 1  5  2  5  8  2  5  7  3 14  6  0]

# Sort the array alphabetically
import numpy as np
b=np.array(['c','d','a','b'])
print(np.sort(b))

# Sorting the 2-D array
import numpy as np
c=np.array([[13,0,1],[2,0,4]])
c1=c.reshape(-1)
print(np.sort(c1))
# this converts it in a 1-D array and then sorts it
print(np.sort(c))
# sorts individual arrays of the 2-D array and gives it out as a 2-D array
# Output: [[ 0  1 13][ 0  2  4]]
