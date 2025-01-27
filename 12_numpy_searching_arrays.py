# Searching array - you can search a certain value and return the indexes that get the match
# by using where()

import numpy as np
a=np.array([1,2,3,4,5,4,4])
a1=np.where(a==4)
print(a1)
# this where function gives indexes of the occurence of 4 in the given array as output in the form of array
# output: (array([3, 5, 6]),)

# Now we will find the indexes where the values are even
import numpy as np
b=np.array([1,2,3,4,5,6,7,8])
b1=np.where(b%2==0)
print(b1)# output : (array([1, 3, 5, 7]),)

# Searchsorted() - performs binary search in array and returns the index of the occurences
# we will find the index where the value 7 should be inserted
import numpy as np
c=np.array([1,2,3,4,5,6,7,8,9])
c1=np.searchsorted(c,7)
print(c1)
# output : 6 returns the index of the occurence in 7


# Now we will search from right side meaning tell the index from the right where the value is found
import numpy as np
d=np.array([1,2,3,4,5,6,7,8,9])
d1=np.searchsorted(d,7,side='right')
print(d1)# Output is 7
print(len(d)-d1) # Output is 2
# with side='right', the insertion point would be after index 6, so the result is 7.

