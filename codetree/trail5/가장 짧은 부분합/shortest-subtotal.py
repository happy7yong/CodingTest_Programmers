n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
cur_sum = 0
min_dist = 100000

for right in range(n) :
    cur_sum += arr[right]

    while cur_sum >= s :
        min_dist = min(min_dist,right-left+1)
        cur_sum -= arr[left]
        left+=1

print(-1 if min_dist==100000 else min_dist)
