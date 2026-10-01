arr = []

num = int(input("Enter size of array: "))

print("Add elements of array:")

for i in range(num):
    a = int(input())
    arr.append(a)

arr.sort()

print("Largest element:", arr[len(arr)-1])
print("Second largest element:", arr[len(arr)-2])
print("Smallest element:", arr[0])
print("Second smallest element:", arr[1])