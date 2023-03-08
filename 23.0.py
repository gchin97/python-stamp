# # a = [[10, 20], [30, 40], [50, 60]]
# # for i in a:
# #     for j in i:
# #         print(j, end=" ")
# #     print()

# # for i in range(len(a)):
# #     for j in range(len(a[i])):
# #         print(a[i][j], end=" ")
# #     print()

# # i = 0
# # while i < len(a):
# #     x, y = a[i] #변수를 두개를 지정하면 두개 다 가져올 수 있음
# #     print(x, y)
# #     i += 1
# # # print()
# # while i < len(a):
# #     j=0
# #     while j< len(a[i]):
# #         print(a[i][j], end=" ")
# #         j+=1
# #     print()
# #     i+=1


# a = []
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
# print(a)

# a = [[0 for j in range(2)]for i in range(3)]
# print(a)


# a = [[[0 for i in range(3)] for j in range(4)] for z in range(2)]
row = int(input())
matrix = []
for i in range(row):
    matrix.append(list(input()))
