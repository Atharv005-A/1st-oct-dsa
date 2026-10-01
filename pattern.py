# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("Enter size: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):

#     for j in range(n - i):
#         print(" ", end=" ")

#     for j in range(1, i + 1):
#         print(j, end=" ")

#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")

#     print()

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()