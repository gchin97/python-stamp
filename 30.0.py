x = [10]
print(*x)


def personal_info(name, age, address):
    print("name:", name)
    print("age:", name)
    print("address:", name)


personal_info("grace", 22, "용산")
print(personal_info)

def minscore(**args):
    min(args)

def maxscore(**args):
    max(args)

def getAverage(**kwargs):
    return(sum(kwargs.value())/len(kwargs))