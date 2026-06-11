a,b = map(int,input().split())
sum=0;
max = max(a,b)
min = min(a,b)
for i in range(min,max+1) :
    if i%5==0 :
        sum+=i
    
print(sum)