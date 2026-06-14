n = int(input())
cnt=0

# 위아래 대칭이고 짝수는 점점 감소하고 홀수는 점점 증가하는 모양
#1 2 3 4 5
for i in range(1,n+1) :
    if i%2!=0 :
        for _ in range(cnt+1) :
            print("*",end=" ")
        print()
        cnt+=1
    else :
        for _ in range(n+1-cnt,0,-1) :
            print("*",end=" ")
        print()

for i in range(n+1,1,-1) :
    if i%2!=0 :
        for _ in range(cnt+1) :
            print("*",end=" ")
        print()
        cnt+=1
    else :
        for _ in range(n+1-cnt,0,-1) :
            print("*",end=" ")
        print()