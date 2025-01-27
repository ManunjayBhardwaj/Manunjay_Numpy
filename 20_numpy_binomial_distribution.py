# Binomial distribution - discrete distribution
# parameters are - n(number of trials), p(probability),size(shape-returned array)

# given 10 trials for a coin which will generate 10 data points:

from numpy import random
a=random.binomial(n=10,p=0.5,size=10)
print(a)

#visualisation of binomial distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
b=random.binomial(n=10,p=0.5,size=1000)
# random.binomial(n=10, p=0.5, size=1000):
# n=10: Each trial consists of 10 independent experiments (e.g., flipping a coin 10 times).
# p=0.5: The probability of success (e.g., getting heads in a coin flip) for each trial is 0.5.
# size=1000: This generates 1000 trials, each with 10 experiments.


# Difference between normal and binomial -
# normal (continous) where binomial(discrete)
sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False,label='Normal')
sns.distplot(random.binomial(n=100,p=0.5,size=1000),hist=False,label='Binomial')
plt.show()
#this print the distplot of both the distributions in one graph with different colors for each distribution
# as the number of observations for both distributions is same therefore the graphs are also quite similar leading to confusion to identification
# to remove this confusion we have to alter the number of observations on both
# therefore use different size values for both the distributions
