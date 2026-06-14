n=int(input())
sum=0

for i in range(1,n+1) :
    if i%2!=0: #홀수
        for j in range(n) :
            sum+=1
            print(sum,end=" ")
        sum=sum+n
    else : #짝수
        for j in range(n) :
            print(sum,end=" ")
            sum-=1
        sum=sum+n
    print()
        