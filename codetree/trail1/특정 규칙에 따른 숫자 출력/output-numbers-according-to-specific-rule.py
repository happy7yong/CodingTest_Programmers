n = int(input())
sum=1;

for i in range(n,0,-1) :
    for j in range(n-i) :
        print(" ",end=" ")
    for j in range(i) :
        if sum==10 :
            sum=1
        print(sum,end=" ")
        sum+=1
    print()