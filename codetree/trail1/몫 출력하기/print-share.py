cnt=0
while True :
    a=int(input())
    if a%2==0:
        print(a//2)
        cnt+=1
    if cnt>=3 :
        break