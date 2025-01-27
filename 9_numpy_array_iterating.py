# iterating array- means going through the elements one by one or step by step, like for loop

# Iterate the elements of 1-D 
import numpy as np
a=np.array([1,2,3,4,5])
for i in range(len(a)):
    print(a[i])

#Simple method
import numpy as np
b=np.array([1,2,3,4,5])
for i in b:
    print(i)
  
# Iterate the elements of 2-D 
import numpy as np
c=np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
for i in range(len(c)):
     for j in range(len(c[0])):
          print(c[i,j])

#Simple method for iterating on each scalar element of the 2-D array
import numpy as np
d=np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
for i in d:
     for j in i:
          print(j)

# Iterate 3-D
import numpy as np
e=np.array([[[1,2,3],[6,7,8]]])
for i in e:
     for j in i:
          for k in j:
               print(k) 

# Complex way of itertation
import numpy as np
f=np.array([[[1,2,3],[6,7,8]]])
for i in range(len(f)):
     for j in range(len(f[0])):
           for k in range(len(f[0][0])):
               print(f[i,j,k])

# Iterating arrays using the nditer() function
# Now we will iterate on each scalar element
# this nditer function simplifies the code and we can directly acces each and 
# every element of the multidimensional array
import numpy as np
g=np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(g):
     print(i)
 
# Now we will iterate with different step sizes
import numpy as np
h=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(h[:, ::2]):
     print(i)
# {np.nditer(h[:, ::2]):} this means that take both arrays of h
# in both the arrays take the whole arrays as the index is not specified 
# take the step size to be 2 meaning every other element is print iteratively 