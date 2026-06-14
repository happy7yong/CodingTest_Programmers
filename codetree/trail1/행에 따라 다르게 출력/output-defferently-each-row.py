n = int(input())
sum=2

for i in range(1,n+1) :
    if i%2!=0: #홀수
        sum-=1
        for j in range(1,n+1) :
            print(sum,end=" ")
            sum+=1
    else : #짝수
        sum+=1
        for j in range(1,n+1) :
            print(sum,end=" ")
            sum+=2


    print()
