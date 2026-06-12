n=int(input())

for i in range(n,0,-1) : 
    for j in range(0,n-i) : #증가
        print(" ",end=" ")
    
    for j in range(2*i-1,0,-1) : #감소
        print("*",end=" ")
    print()