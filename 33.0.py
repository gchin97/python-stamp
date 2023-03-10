def counter():
    i=0
    def count():
        nonlocal i
        return i
        i+=1
    return count

def countdown(n):
    i=n+1
    def count():
        nonlocal i
        return i
        i-=1
    return count