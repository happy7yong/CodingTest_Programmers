n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_cnt = 0
cnt = 0

for i in range(n) :
    if arr[i-1]>t :
        cnt+=1
    elif i>0 and (arr[i-1] > t and arr[i] > t) :
        cnt+=1
    else :
        cnt=0
    max_cnt = max(max_cnt,cnt)

print(max_cnt)