def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


for i in number_generator(3):
    print(i)


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def three_generator():
    yield from number_generator(3)


for i in three_generator():
    print(i)

# 파일 file 객체를 사용함


def file_read():
    with open("words.txt") as file:
        # 파일에 저장된 줄 수에 상관없이 읽으려면 while =True라는 무한 루프가 필요함
        while True:
            line = file.readline()
            if line == "":
                break
            yield line.strip("\n")


line strip
