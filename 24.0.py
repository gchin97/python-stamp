# x= path.split("\\")
# print(x[-1])


n=list(map(int, input().split(";")))
n.sort(reverse=True)
# list를 만들어서 진행
for i in n:
    print("{0:>9,}" .format(i))

