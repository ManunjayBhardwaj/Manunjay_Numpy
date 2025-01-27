# Slicing array - slicing in python means taking elements from one given index to another index
# [start:end],[start:end:step]

# now we will slice an element from 1 to 5:
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[1:5])
# this slicing ignores the ending index and includes the starting index
# therefore the output of the above statement will be : [2 3 4 5]

# now we will slice from index 4 to the end value
print(a[4:])# here the last value is not ignored 

# now we will slice from the starting index to the 5th value
print(a[:5])# here the value at 5th index is ignored

# Negative slicing - index 3 to end
import numpy as np
b=np.array([1,2,3,4,5,6,7,8,9])
print(b[-6:-1])
# here the value at the -3 index is included while the value at -1 index is always ignored
# this means that the starting index value is always considered while the ending index value is ignored

# Step: you will use steps value to determine the step of the slicing
import numpy as np
c=np.array([1,2,3,4,5,6,7,8,9])
print(c[1:5:2]) # this returns every other value from index 1 to 5 
# therefore the output will be :[2 4]

# now return every other from the entire array
print(c[ : :2]) 

# Slicing a 2-D array
import numpy as np
d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(d[1][1:4]) # output:[7 8 9]
# this loc means that we will slice the second array from 1 to 4 index

print(d[0,1:4])# output:[2 3 4]
# this loc means that we will slice the first array from 1 to 4 index


#Imp
import numpy as np
e=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(e[0:2,1:3])
# this means that we are outputting values from the first index to the third from both the arrays as we can slice in these arrays too
# for eg
import numpy as np
f =np.array([[1,2,3,4,5],[6,7,8,9,10],[1,3,5,7,9],[2,4,5,6,7]])
#now i want elements from the first index to the third index from the 2nd and 3rd array
print(f[1:3,1:4])