# Random Meaning- something that can not be predicted logically

# now we will generate a random number from 0 to 100
from numpy import random # we are importing the sub library called random from numpy
a=random.randint(100)# prints a random integer from 0 to 100
print(a)

# You can generate float() via rand()
from numpy import random 
b=random.rand()# prints a random floating value from 0 to 1 if value is not specified
print(b)

# You can also generate random array
# We will generate a 1-D array containing 5 random integers from 0 10 100
from numpy import random 
c=random.randint(100,size=(5))# prints a random integer array
print(c)

# We will generate a 2-D array having 3 rows each  containing 5 random integers from 0 10 100
from numpy import random 
d=random.randint(100,size=(3,5))# prints a random 2-D integer array
print(d)

# We can also generate random numbers from an array
# using choice()
from numpy import random 
e=random.choice([3,5,6,8,9,23,41,1])
print(e)
# random.choice() picks a random value from the specified array in the choice method

# We can also generate random numbers from a 2-D array
# using choice()
from numpy import random 
f=random.choice([1,2,3,4,5,6,7], size=(3,5))
# this line of code means that we are asking the choice function to make a 2-D array 
# having 3 rows and rach row having 5 elements each and these values shall be picked from the given specified array
print(f)# output : [[6 3 4 1 3][5 1 5 3 4][3 3 6 1 1]] this is a random value written here just to define that we get and 
#output as a 2-D array having values from the given array
