# def add_sub(a, b):
#     return a+b, a-b


# x, y = add_sub(10, 20)
# print(x, y)

def mul(a, b):
    c = a*b
    return c


def add(a, b):
    c = a+b
    print(c)
    d = mul(a, b)
    print(d)


x = 10
y = 20
print(add(x, y))
