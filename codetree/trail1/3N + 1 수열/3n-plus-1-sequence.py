n=int(input())
cnt=0

while True :
    #트리거
    if n==1 :
        break;

    if n%2==0 : 
        n//=2
    else :
        n=n*3+1
    cnt+=1

print(cnt)