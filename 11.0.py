# # 연산자
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[2])
# print(a.__getitem__(2))
# print(a[(len(a)-1)])
# print(a[0:2])
# print(a[:])
# print(a[:len(a)])


# n[1:len(n):2]

# x = input().split()
# del x[-5:]
# print(tuple(x))

# 0으로 시작해서 2번째부터 세면 짝수,
# 1로 시작해서 2번째부터 세면 홀수

# x = input().split()
# del (x[0:len(x):2])
# y = input().split()
# del (y[0:len(y):2])
# print(x[1::2]+y[0::2])

lux = dict(zip(["name", "brand"], ["prada", 20]))
print(lux)

keys = input().split()
value = list(map(float, input().split))
result = dict(zip(keys, value))
print(result)
