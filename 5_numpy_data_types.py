# data types in python : string,integer,boolean,float,complex
# data types in numpy
  # i for integer
  # b for boolean
  # u for unsigned integer
  # f for float
  # c for complex float
  # m for timedelta
  # M for datetime
  # O for object
  # S for strings
  # U for unicode strings
  # v for memory

# checking the data type of numpy array: dtype
import numpy as np
a=np.array([1,2,3,4])
print(a.dtype)# this gives output as int64

# checking the data type of numpy array-string
import numpy as np
b=np.array(["apple","banana","cherry"])
print(b.dtype) # this will give output as U6 meaning unicode strings

# creating array with a defined data type: 
import numpy as np
c=np.array([1,2,3,4],dtype="S")
# this concatenates the string and integer and then give output as 
# [b'1' b'2' b'3' b'4']
print(c)
print(c.dtype)# and this will give output as S1

#now we will create an array with data type of 4 byte int:
import numpy as np
d=np.array([1,2,3,4],dtype="i4")
print(d.dtype)
# this assigns the integer value to be of 4 bytes therefore 32 bits
# therefore the output is int32

# if a type is given in which the elements cannot be casted then numpy will raise an error
# what if a value cannot be converted?

# import numpy as np
# e=np.array(["a","2","3"],dtype="i")
# print(e.dtype)
# this will raise an error as the 2 and 3 in the array will be converted into integers as they are integer values in this array as string 
# but the a in this cannot be converted to an integer as it is not an integer value in the array

# Converting datatype in existing array - astype()
import numpy as np
e=np.array([1.1,2.3,3.5,4.5])
e1=e.astype("int")
print(e1)# output:[1 2 3 4]
print(e1.dtype)# output:int32
#this means that we make a copy of e array in this e1 variable and then we copy the elements of the array as the desired data type

# Converting data type from integer to boolean
import numpy as np
f=np.array([1,0,3,4])
f1=f.astype('bool')
print(f1) # output:[ True False  True  True] as 0 is false else everything is true
print(f1.dtype) # oiutput : bool