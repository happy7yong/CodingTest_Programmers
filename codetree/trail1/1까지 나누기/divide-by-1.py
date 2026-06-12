n = int(input())
cnt=1
next=n;

while True :
    next = next//cnt
    if next <= 1 :
        break
    cnt+=1
print(cnt)