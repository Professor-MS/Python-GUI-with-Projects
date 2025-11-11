# insertion Sort Algorithm
import numpy as np
list1 = [1,2,3,4,5]
array1 = np.array([3,7,2,5,1,4])
i=2
for i in range(len(array1+1)):
    key=array1[i]
    j=i-1
    while (array1[i]>key and j>1):
        array1[j+1]=array1[j]
        j=j-1
j=j+1
array1[j]=key


print(array1)