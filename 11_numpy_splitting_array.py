# Splitting arrays in numpy- It is reverse to joining, breaking the array
# array.split() function is used


# splitting the 1-D array into 3 parts
import numpy as np
a=np.array([1,2,3,4,5,6])
a1=np.array_split(a,3)
print(a1)
# the output comes out as [array([1, 2]), array([3, 4]), array([5, 6])]

# now we will split this ame array in 4 parts
import numpy as np
b=np.array([1,2,3,4,5,6])
b1=np.array_split(b,4)
print(b1)
# the output comes out as :[array([1, 2]), array([3, 4]), array([5]), array([6])]
# it first breaks the first four elements into 2 parts and the rest two into single elements
# the functionality lies in the array_split() function of automatic splitting and not in the sinple split function


# Split into array with index
import numpy as np
c=np.array([1,2,3,4,5,6])
c1=np.array_split(c,4)
print(c1)# Output:[array([1, 2]), array([3, 4]), array([5]), array([6])]
print(c1[0])# Output:[1 2]
# as the output is an array itself therefore we can access each element of the array using the index
# the print statement prints the first index of the splitted output array

# Splitting the 2-D array
import numpy as np
d=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
d1=np.array_split(d,3)
print(d1)
# this split function will split the 2-D array into 3 different 2-D arrays
# therefore the output is [array([[1, 2],[3, 4]]), array([[5, 6],[7, 8]]), array([[ 9, 10],[11, 12]])]

# if we want to access each single array
print(d1[0][0])# Output:[1 2]
print(d1[2][1]) # Output :[9 10]
print(d1[2][0][0])# Output:9

# Splitting the 2-D into three 2-D along with rows (Column Stacking)
import numpy as np
e=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
e1=np.array_split(e,3,axis=1)
print(e1)
#this wil stack all the columns of the 2-D array and return each column as an 2-D array of each element for the output
# Output:[array([[ 1],[ 4],[ 7],[10],[13],[16]]), array([[ 2],[ 5],[ 8],[11],[14],[17]]), array([[ 3],[ 6],[ 9],[12],[15],[18]])]

# Alternate solution is using the hsplit(), opposite hstack()
import numpy as np
f=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
f1=np.hsplit(e,3)
print(f1)
# this obtains the same output as the above : np.array_split(e,3,axis=1)

