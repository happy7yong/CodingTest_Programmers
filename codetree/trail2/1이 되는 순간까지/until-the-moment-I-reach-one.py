n = int(input())

def program(n) :
    if n%2==0 :
        return n//2
    else :
        return n//3

def f(n) :
    #종료조건
    if program(n) == 1 :
        return 1
    if n<=1 :
        return 0
    
    return f(program(n)) + 1

print(f(n))