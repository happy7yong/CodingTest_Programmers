n=int(input())

for i in range(n,0,-1) : #감소
    for j in range(i,0,-1) : #감소
        print("*",end="")
    for j in range(0,2*(n-i)) : #증가
        print(" ",end="")
    for j in range(i,0,-1) : #감소
        print("*",end="")
    print()