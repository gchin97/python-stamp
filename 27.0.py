# file = open("hello.csv", "w")
# file.write("a,b,c,d")
# file.close()

# file = open("hello.csv", "r")
# # 변수를 만들어서 파일을 읽어서 변수안에 넣어둠
# s = file.read()
# print(s)
# file.close()

# close 없이 파일 열고 닫기 - with as
# with open("hello.csv", "r") as file:
#     s = file.read()
#     print(s)

import pickle
with open("hello.csv", "w") as file:
    for i in range(0, 3):
        file.write("hello, world {0}\n".format(i))


lines = ['hello\n', 'i am \n', 'summer\n']
# 리스트에 들어있는 문자열을 넣어줌 - writelines
with open("hello.csv", "w") as file:
    file.writelines(lines)


# 리스트에 들어있는 문자열을 넣어줌 - writelines
with open("hello.csv", "r") as file:
    lines = file.readlines()
    print(lines)

with open("hello.csv", "r") as file:
    line = None
    while line != "":
        line = file.readline()
        print(line.strip("\n"))

with open("hello.csv", "r") as file:
    for line in file:
        print(line.strip("\n"))

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open("hello.p", "w") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open("words.txt", "r") as file:
    count = 0
    lines = file.readlines()
    for line in lines:
        if len(word.strip("\n")) <= 10:
            count += 1
    print(count)

with open("words.txt", "r") as file:
    words = line.split()
    for word in words:
        if "c" in word:
            print(word.strip(",."))
