n=int(input())

for i in range(n,0,-1) : #한번 돌때 감소 첫값이 제일 큼
    for j in range(n-i) : #증가
        print(" ",end=" ")

    for j in range(2*i-1) : #감소
        print("*",end=" ")
    
    print()

for i in range(2,n+1) : #한번 돌때 감소 첫값이 제일 큼
    for j in range(n-i) : #증가
        print(" ",end=" ")
        
    for j in range(2*i-1) : #감소
        print("*",end=" ")
    
    print()
