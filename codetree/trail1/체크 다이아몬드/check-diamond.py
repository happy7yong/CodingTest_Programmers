n=int(input())

for i in range(1,n+1) : #증가
    for _ in range(n-i) : #감소
        print(" ",end="")
    for _ in range(i) :
        print("*",end=" ")
    print()

for i in range(n-1,0,-1) : #증가
    for _ in range(n-i) : #감소
        print(" ",end="")
    for _ in range(i) :
        print("*",end=" ")
    print()