n = int(input())
sum=0;
avg=0;
cnt=0

for _ in range(n):
    sum+=int(input())
    cnt+=1

print(sum,round(sum/cnt,1))