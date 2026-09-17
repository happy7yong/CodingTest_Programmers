X, Y = map(int, input().split())

cnt=0

def isPellin(x_int) :
    x=list(map(int,list(str(x_int))))
    if len(x)%2==0 :#짝수
        k = len(x)//2
        for i in range(1,k+1) :
            if x[k-i] != x[k + (i-1)] :
                return 0
        return 1


    elif len(x)%2!=0 :#홀수
        k = len(x)//2 #중앙값
        for i in range(1,k+1) :
            if x[k+i] != x[k-i] : #같지 않다면 팰린드롬 아님!
                return 0
        
        return 1
            

for i in range(X,Y+1) :
    if isPellin(i) :
        cnt+=1

print(cnt)