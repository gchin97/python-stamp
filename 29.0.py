# # def add_sub(a, b):
# #     return a+b, a-b


# # x, y = add_sub(10, 20)
# # print(x, y)

# def mul(a, b):
#     c = a*b
#     return c


# def add(a, b):
#     c = a+b
#     print(c)
#     d = mul(a, b)
#     print(d)


# x = 10
# y = 20
# print(add(x, y))

# def get_quotient_remainer(x,y):
#     a=x/y
#     b=x%y
#     return a,b


x, y = map(int, input().split())


def cal(x, y):
    a = x+y
    s = x-y
    m = x*y
    d = x/y
    return a, s, m, d


a, s, m, d = cal(x, y)


print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
