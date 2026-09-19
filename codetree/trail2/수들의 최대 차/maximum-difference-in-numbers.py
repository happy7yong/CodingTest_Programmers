n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]


arr.sort()
max_len = 0


l=0
#투포인터: 확장담당
for r in range(n) :
    #복구 중 :
    while arr[r]-arr[l] > k :
        l+=1
    
    max_len = max(max_len,abs(l-r)+1)

print(max_len)
