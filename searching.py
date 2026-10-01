arr=[]
num=int(input("enter size of array:"))
print("add elements of array:")
for i in range (num):
    a=int(input())
    arr.append(a)

key=int(input("enter element to search:"))

for i in arr:
    if key==i:
        print("element is present at",arr.index(i)+1," postion")