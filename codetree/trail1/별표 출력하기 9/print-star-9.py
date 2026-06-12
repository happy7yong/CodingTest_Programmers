n=int(input())

for i in range(1,n+1) : #증가
    for j in range(n-i,0,-1) : #감소
        print(" ",end=" ")
    
    for j in range(2*i-1) : #증가
        print("*",end=" ")
    print()
