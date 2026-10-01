arr=[]
num=int(input("enter size of array:"))
print("add elements of array:")
for i in range (num):
    a=int(input())
    arr.append(a)
sum=0
for i in arr:
    sum=sum+i
print("sum of all array elements:",sum)