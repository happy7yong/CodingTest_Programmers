cnt = 9
n = int(input())

for _ in range(n) :
    for j in range(n) :
        if cnt==0 :
            cnt=9
        print(cnt,end="")
        cnt-=1
    print()