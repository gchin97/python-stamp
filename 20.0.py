# 특히 문자열에 True를 곱하면 문자열이 그대로 나오고, False를 곱하면 문자열이 출력되지 않습니다(True는 1, False는 0으로 연산
# >>> 'Fizz' + 'Buzz'
# 'FizzBuzz'
# >>> 'Fizz' * True
# 'Fizz'
# >>> 'Fizz' * False
# ''

start, stop = map(int, input().split())
for i in range(start, stop+1):
    if i % 5 == 0 and i % 7 == 0:
        print("fizz buzz")
    elif i % 5 == 0:
        print("fizz")
    elif i % 7 == 0:
        print("buzz")
    else:
        print(i)
