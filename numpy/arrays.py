#adding the element in array
import array as arr
x=range(3,100)
arr=arr.array("i",x)
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")
#insert the element
arr.insert(0,2)
arr.insert(0,1)
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")

#append the elementss..
arr.append(100)
arr.append(200)
for i in range(0,len(arr)):
    print(arr[i],end=" ")


import array as arr
arr=arr.array("i",[1,2,3,4,5,6,7,8,9])
for num in arr:
    print(num,end=" ")
print("/n")

arr[1]=1
for num in arr:
    print(num,end=" ")


import array as arr
x=range(1,10)
arr=arr.array("i",x)
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("/n")
arr[3]=3
for i in range(0,len(arr)):
    print(arr[i],end=" ")


#deleting the elements.....
import array as arr
arr=arr.array("i",[1,2,3,4,5,6,7,8])
for num in arr:
    print(num,end=" ")
print("/n")
arr.pop()
arr.remove(1)
for num in arr:
    print(num,end=" ")


#slicing the elements,.....
import array as arr
arr=arr.array("i",[1,2,3,4,5,6,7,8])
for num in arr:
    print(num,end=" ")
print("/n")
arr1=arr[1:6]
arr1=arr[1:-1]
for num in arr1:
    print(num,end=" ")
print("/n")

import array as arr
x=range(0,100,3)
arr=arr.array("i",x)
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("/n")
arr1=arr[8:17]
arr1=arr[::-1]
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print("/n")    

#searching the elements and index.....
import array as arr
x=range(0,1000,4)
arr=arr.array("i",x)
for num in arr:
    print(num,end=" ")
print("/n")
index=arr.index(900)
res=arr[index]
print("the index is:",index,"the element is:",res)

import array as arr
arr=arr.array("i",[2,6,8,0,7,9,1,4,3,5])
for num in arr:
    print(num,end=" ")
print("/n")
arr1=sorted(arr)
arr2=sorted(arr,reverse=True)
for num in arr1:
    print(num,end=" ")
print("/n")
print(arr2)