

# def number_generator():
#     yield 0
#     yield 1
#     yield 2 #값을 발생시킴


# for i in number_generator():
#     print(i)


def number_generator():
    yield 0
    yield 1
    yield 2  # 값을 발생시킴


g = number_generator

a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)

# return과는 다르게 값을 보낸 후에 다시 제너레이터 안으로 들어옴
