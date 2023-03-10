# 재귀호출 함수

def hello(count):
    if count == 0:
        return
    print("hi", count)
    count -= 1
    hello(count)

# 계속 할 시 오류가 나타남


hello(5)


def is_pal(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    print(word[1:-1])

# factorial 구하기


def factorial(n):
    if n == 1:
        return
    return n*factorial(n-1)


def fibonacchi(n):
    if n <= 1:
        return n
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)

    # if i in range(0,n+1):
    #     x= n[i]+n[i+1]
    #     x++;
    # print(x)
