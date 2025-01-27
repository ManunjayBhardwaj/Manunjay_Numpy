# matplotlib(pyplot)- seaborn
# seaborn is a library that uses matplotlib underneath to plot graph that is pyplot

# Distplot- distribution plot(curve plot-histogram)
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()

# Plotting a displot without the histogram we just add and attribute to the sns.distplot(hist=False)
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
a=random.randint(100,size=(100))
sns.distplot(a,hist=False)
plt.show()