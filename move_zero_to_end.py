arr = []

num = int(input("Enter size of array: "))

print("Add elements of array:")

for i in range(num):
    a = int(input())
    arr.append(a)

newarr = []

for i in arr:
    if i != 0:
        newarr.append(i)

for i in arr:
    if i == 0:
        newarr.append(i)

print(newarr)