n = int(input())
cnt = 0

#홀수 : n부터 점점 감소
#짝수 : n부터 점점 증가
# 1 2 3 4 5
for i in range(1,n+1) :
    if i%2==0:#짝수
        for _ in range(cnt) :
            print("*",end=" ")
        print()
    else :#홀수
        for _ in range(n-cnt) :
            print("*",end=" ")
        cnt+=1
        print()

for i in range(n+1,1,-1) :
    if i%2==0:#짝수
        for _ in range(cnt) :
            print("*",end=" ")
        print()
    else :#홀수
        for _ in range(n-cnt) :
            print("*",end=" ")
        cnt+=1
        print()