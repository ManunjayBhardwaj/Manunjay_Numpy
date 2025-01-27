# Normal Distribution(Gaussian Distribution)- very important
# random.normal() method- mean(loc),standard deviation(scale),size

# we are generating a random normal distribution of size 2*3
from numpy import random
a=random.normal(size=(2,3))
print(a)

# we are generating a random normal distribution of size 2*3, mean =1 and standard deviation of 2:
from numpy import random
b=random.normal(loc=1,scale=2,size=(2,3))
print(b)

# Visualisation a normal distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
c=random.normal(loc=1,scale=2,size=(100))
sns.distplot(c,hist=False)
plt.show()

# The curve of a Normal Distribution is also called a bell curve 