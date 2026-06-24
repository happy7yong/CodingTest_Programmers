n = int(input())

#n이 짝수이면 2부터 N까지
def f2(n) :
    if n<=0 :
        return 0
    if (n)%2==0:
        return f2(n-1) + n
    
    return f2(n-1)

def f1(n) :
    if n<=0:
        return 0
    if (n)%2!=0:
        return f1(n-1) + n
    
    return f1(n-1)


if n%2==0 :
    print(f2(n))
else :
    print(f1(n))

