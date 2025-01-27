# Joining the numpy array - 
# here for this we will pass concatente()

# Using this concatenate we can easily add two 1-D arrays
import numpy as np
a=np.array([1,2,3])
a1=np.array([4,5,6])
a2=np.concatenate((a,a1))
print(a2)


# Joining of 2-D arrays along with rows (axis=1)
# Column Stacking
import numpy as np
b=np.array([[1,2],[3,4]])
b1=np.array([[5,6],[7,8]])
b2=np.concatenate((b,b1),axis=1)
#this axis=1 means that it will join the elements row wise
print(b2)
# output is [[1 2 5 6][3 4 7 8]] see here along the rows the columns are binded
# To concatenate along axis=1 (column stacking), the arrays must have the same number of rows.


# Joining of 2-D arrays along with columns (axis=0)
# Row Stacking
b3=np.concatenate((b,b1),axis=0)
print(b3)
# output is [[1 2][3 4][5 6][7 8]] they are stacked row wise
# For axis=0 (row stacking), the arrays must have the same number of columns.

# Joining array using the stack function
import numpy as np
c=np.array([1,2,3])
c1=np.array([4,5,6])
c2=np.stack((c,c1),axis=1)
print(c2)
# the stack function works on indexes of individual arrays 
# here it gives this as output by stacking indexes : [[1 4][2 5][3 6]]

# Stacking along with rows (Column Stacking): hstack()
import numpy as np
d=np.array([1,2,3])
d1=np.array([4,5,6])
d2=np.hstack((d,d1))
print(d2)
# hstack directly gives the output : [1 2 3 4 5 6] as there is only one column

# Stacking along with columns (Row Stacking): vstack()
import numpy as np
e=np.array([1,2,3])
e1=np.array([4,5,6])
e2=np.vstack((d,d1))
print(e2)
# here the output is will be both the rows are stacked along with the columns therefore we will recieve 
# output as : [[1 2 3][4 5 6]]

# Stacking along with height(depth)
import numpy as np
f=np.array([1,2,3])
f1=np.array([4,5,6])
f2=np.dstack((d,d1))
print(f2)
# this function will directly give output as concatenating on the basis of height
# Output is [[[1 4][2 5][3 6]]]