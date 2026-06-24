n = int(input())

def magicNumber(n) :
    if n%2==0 :
        return n//2
    else :
        return n*3+1
    
def f(n) :
    if n==1 :
        return 0
    return f(magicNumber(n)) + 1

print(f(n))