start, stop = map(int, input().split())
i = start
while True:
    # range(start,stop)
    if i % 10 == 3:
        continue
    if i > stop:
        break
    print(i, end="")
    i += 1
