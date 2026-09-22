n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [float('inf')] * n

#dp로 풀어야할 것 같음.
#dp[i] : i까지 오는데 지나온 돌의 최댓값 / 중 최솟값
#max(dp[j],arr[i])
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

for curIdx in range(2,n) : #dp 배열에 있는거 탐색해 볼까  i=현재 값 
    for dist in range(1,k+1) : #j는 이동거리
        preIdx = curIdx-dist #다음 인덱스는 현재인덱스 + 거리
        if preIdx >= 0 :
            dp[curIdx]=min(dp[preIdx],dp[curIdx])
    dp[curIdx] = max(dp[curIdx],arr[curIdx])

    


print(dp[n-1])