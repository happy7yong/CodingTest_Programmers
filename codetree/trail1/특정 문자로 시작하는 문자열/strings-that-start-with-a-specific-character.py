n = int(input())

arr = [ input() for _ in range(n)]

ch = input()
cnt=0
sum=0

for ele in arr :
    if ch == ele[0] :
        cnt+=1
        sum+=len(ele)

print(cnt, f"{sum/cnt:.2f}")