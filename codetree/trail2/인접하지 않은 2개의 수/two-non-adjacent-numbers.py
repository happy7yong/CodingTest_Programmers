#내가 뭘 구하려고 하는가 : 인접하지 않는 2개의 수를 선택해서 합 최대
#내가 할 수 있는 행동 : 투포인터로 선택해야하는가? DP로 할 수 있을 것 같은데? 바텀업 방식으로
#반복 조건 : 2개의 수를 선택해서 합
#제외 조건 : 인접하면 안됨
#사용할 수 있는 for :
#정답 갱신 : 최댓값

#dp 템플릿
#dp[i] : i에 있는 값이 남아있는 왼쪽 수 중 본인을 포함해 인접하지 않는 수를 선택했을때 얻을 수 있는 최댓값
#dp 점화식 : dp[3]일 경우 dp[1]+arr[3],dp[0]+arr[3] 중에서 선택
#dp[i]는 dp[i-1]만 아닌 경우 모두 더해볼수있다.->max(dp[0],dp[1],[2] ...)
n=int(input())
arr = list(map(int,input().split()))

max_val = 0

for first_p in range(n-2) :
    for last_p in range(first_p+2,n) :
        max_val = max(max_val,arr[first_p]+arr[last_p])

print(max_val)