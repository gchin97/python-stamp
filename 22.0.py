# a = [10, 20, 30]
# a.append(40)
# print(a)
# a.append([50, 60])
# print(a)
# a.insert(2, 35)
# print(a)
# a.insert(len(a), 100)  # len(a)는 항상 마지막 인덱스보다 1 크기 땜에 마지막에 넣는 것으로 사용

# print(a)


# if 조건문을 활용하여 리스트에 요소가 있을 때만 마지막 요소를 가져오면 됨

# seq = []
# if seq:               # 리스트에 요소가 있는지 확인
#     print(seq[-1])    # 요소가 있을 때만 마지막 요소를 가져옴

# a = [30, 21, 52, 63, 14]
# smallest = a[0]
# for i in a:
#     if i < smallest:
#         smallest = i
# print(smallest)

# b = list(i for i in range(10))
# print(b)
# a = [i*j for j in range(2, 10) for i in range(1, 10)]
# print(a)

# c = list(map(str, range(1, 10)))
# print(c)

# b= [i for i in a if len(a)==5]

# make it as a list
start, end = map(int, input().split())
_list = list(2**i for i in range(start, end + 1))
del _list[1]
del _list[-1]
print(_list)


start, end = map(int, input().split())
calculation = list(2**i for i in range(start, end+1))
print(calculation)
