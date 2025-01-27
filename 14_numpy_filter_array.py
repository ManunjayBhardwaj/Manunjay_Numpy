# Getting some elements out of an existing array and curating a new array is called filtering
# A boolean index list is a list of boolean corresponding to indexes in the array - True and False

# create an array from the element on index 0 to 2
import numpy as np
a=np.array([41,42,43,44])
a1=[True,False,True,False]
a2=a[a1]# maps the normal array to the boolean array by index
print(a2)# output : [41 43]
# the above line of code gives output only as the corresponding indexes of true 


# Now we will create a filter array
# that will return only values higher than 42
import numpy as np
b=np.array([41,42,43,44])
empty_list=[]
for i in b:
    if(i>42):
        empty_list.append(True)
    else:
        empty_list.append(False)
# this for loop creates a boolean list that corresponds to our filter 
final_mapped_list=b[empty_list]  
# Each and every time we make a new variable and pass the boolean list inside the main working list as index
# Syntax : new_list=main_list[boolean_list]
print(final_mapped_list)# Prints the filtered array           


# Create a filter that only returns even elements from the original array
import numpy as np
c=np.array([41,42,43,44])
empty_list_2=[]
for i in b:
    if(i%2==0):
        empty_list_2.append(True)
    else:
        empty_list_2.append(False)
final_mapped_list_2=c[empty_list_2]   
print(final_mapped_list_2)      


# Yes , we can directly create a filter from array
# that will return values only higher than 42
import numpy as np
d=np.array([41,42,43,44])
empty_list_3= d>42# by using this statement we skip the process of using a for loop and we directly check our condition on the original array and store it in an empty list
# this will by default create a boolean array
finally_mapped_list_3=d[empty_list_3]
print(finally_mapped_list_3)

# same for even values ( works the same without using for loops)
import numpy as np
e=np.array([41,42,43,44])
empty_list_4= (e%2==0)# by using this statement we skip the process of using a for loop and we directly check our condition on the original array and store it in an empty list
# this will by default create a boolean array
finally_mapped_list_4=d[empty_list_4]
print(finally_mapped_list_4)