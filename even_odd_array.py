arr=[]
num=int(input("enter size of array:"))
print("add elements of array:")
for i in range (num):
    a=int(input())
    arr.append(a)


evenarr=[]
oddarr=[]

for i in arr:
    if i%2==0:
        evenarr.append(i)
    else:
        oddarr.append(i)

print("count of even elements in array are:",len(evenarr))
print("count of odd elements in array are:",len(oddarr))