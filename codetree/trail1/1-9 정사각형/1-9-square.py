n = int(input())
cnt=1

for i in range(1,n+1) :
    for _ in range(n) :
        if cnt>=10 :
            cnt=cnt//10
        print(cnt,end="")
        cnt+=1
    print()