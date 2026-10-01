arr=[]
num=int(input("enter size of array:"))
print("add elements of array:")
for i in range (num):
    a=int(input())
    arr.append(a)

ascarr=arr.sort()
print("largest element:",ascarr[(len(ascarr))])
print("second largest element",ascarr[(len(ascarr)-1)])
print("smallest elment",ascarr[0])
print("second smallest element",ascarr[1])


