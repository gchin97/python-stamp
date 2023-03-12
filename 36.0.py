

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


a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)
