a, b = map(int, input().split())

def program(a,b) :
    if a>b :
        b+=10
        a*=2
    else :
        b*=2
        a+=10
    return a,b

a,b= program(a,b)
print(a,b)