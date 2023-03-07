# import random

# random.randint(a,b) #a,b 모두 포함

# while 1:    # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
#     print('Hello, world!')

# while 'Hello':    # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
#     print('Hello, world!')


balance = int(input())
while balance > 0:
    balance -= 1350
    print(balance)
