sum=0
cnt=0
while True :
    a=int(input())
    if a//10!=2 :
        print(f"{sum/cnt:.2f}")
        break;
    sum+=a
    cnt+=1