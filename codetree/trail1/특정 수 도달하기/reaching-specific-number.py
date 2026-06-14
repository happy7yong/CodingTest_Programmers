arr = list(map(int,input().split()))
sum=0
cnt=0

for ele in arr :
    if 250<=ele :
        break
    sum+=ele
    cnt+=1

print(sum, round(sum/cnt,1))
    