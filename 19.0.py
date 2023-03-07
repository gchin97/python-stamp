# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print("", end=" ")
#         else:
#             print("*", end=" ")
#     print()

n = int(input())
for i in reversed(range(n)):
    for j in range(n):
        if j < i:
            print("", end=" ")
        else:
            print("*", end=" ")
    print()
