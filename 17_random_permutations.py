# Permutation refers to an arrangement of elements like [3,2,1] is permutation of[1,2,3] and vice versa
# the numpy random module provides 2 methods : shuffle() and permutation()

# shuffle() makes changes to the original array
# Now we will randomly shuffle elements for the below array
from numpy import random
import numpy as np
a=np.array([1,2,3,4,5])
random.shuffle(a)
print(a)


# permutation() does not make changes to the original array 
# used majorly for testing purposes
# to obtain permutation we have to make a copy of the original array
# Now we will generate permutation of elements for the below array
from numpy import random
import numpy as np
b=np.array([1,2,3,4,5])
b1=random.permutation(a)
print("This prints the original array as no changes are made on it :",b)
print("To permutate you have to generate a copy and then you can get the output like this",b1)