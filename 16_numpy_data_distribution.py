# Data Distribution is a list of all possible values and how often each value occur
# Such lists are important when working with Data Science and Statistics

# Random distribution: Probability function.

# now we will generate a 1-D array containing 100 values where each value has to be 3,5,7,9
# the probability for the value 3 is set to be 0.3
# the probability for the value 5 is set to be 0.1
# the probability for the value 7 is set to be 0.4
# the probability for the value 9 is set to be 0.2

# the sum of all probability numbers should be 1

from numpy import random
a=random.choice([3,5,7,9], p=[0.3,0.1,0.4,0.2], size=(100))
print(a)
# by using the p attribute we define the probabilities of occurence of the values from the defined array

# Now we will return 2-D with 3 rows each containing 5 values
from numpy import random
b=random.choice([3,5,7,9], p=[0.3,0.1,0.4,0.2], size=(3,5))
print(b)