#numpy......
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[6,7,8]])
print(arr)

zero=np.zeros((3,2))
print(zero)

one=np.ones((2,3))
print(one)

ind=np.eye(4)
print(ind)

import numpy as np
arr=np.array([1,2,3,4,5])
for i in arr:
    print(i,end=" ")
print("/n")
arr[1]=1
for i in arr:
    print(i,end=" ")
print("/n")
arr1=np.delete(arr,1)
print(arr1)

arr2=np.append(arr,4)
print(arr2)

arr3=np.insert(arr,1,2)
print(arr3)

arr4=np.sort(arr)
print(arr4)

arr5=arr[::-1]    #in numpy array there is no reverse sorted array insited of use slicing 
print(arr5)


#maths operation.....
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
addition=np.add(a,b)
print(addition)
sub=np.subtract(a,b)
print(sub)
mult=np.multiply(a,b)
print(mult)


#propertiess...
import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)


#indexing and sllicing
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[0:2,2])
print(arr[1:3,1])
print(arr[2,2])
print(arr[2,1])
print(arr[2,1:3])


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
arr1=np.array([1,2,3])
print(arr+arr1)
print(arr.mean())
print(arr.max())
print(arr.min())


#reshape....
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[4,6,7]])
print(arr)
print(arr.shape)
print(arr.reshape(3,4))
print(arr.reshape(1,12))


import numpy as np
print(np.random.randn(2,3))
print(np.random.randn(3,3))
print(np.random.randn(4,4))


data=np.array([1,1,1,0,0,0,0,0,0,1])
np.random.shuffle(data)
train=data[:6]
test=data[6:]
print("train:",train)
print("test:",test)


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[4,6,7]])
print(arr)
np.linspace(2,3,5)
import random
import numpy as np
Bus_seat=5
while Bus_seat>0:
    print(f"{Bus_seat} seat are avalable")
    seat=input("Do you want to book seat?(yes or no):").lower()
    if seat=="yes":
        name=input("enter your name:")
        Bus_seat-=1
        print(f"{name} your seat is booked sucesfully.....")
        sn=np.random.randint(1,5)
        print("the remaining seat is:",Bus_seat)
        print("your seat number is:",sn)
        break
    else:
        print("not booked")
        break

else:
    print("all seat is booked....")