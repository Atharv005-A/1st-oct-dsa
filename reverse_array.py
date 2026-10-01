arr=[]
num=int(input("enter size of array:"))
print("add elements of array:")
for i in range (num):
    a=int(input())
    arr.append(a)


print("original array",arr)
print("reversed array",arr[::-1])