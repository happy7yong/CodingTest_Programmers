n=int(input())

for i in range(1,n+1) :
    if i%2==0 : #짝수일경우 뽑기
        for _ in range(i) : print("*",end=" ")
    else :
        print("*",end=" ")
    print()