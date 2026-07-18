n = int(input())

dp = [0]*(45+1)

#메모이제이션 필요함
#유형 : dp
#현재 i 에서는 : 이전 두항의 합을 합친다. dp[i] = d[i-1] + dp[i-2]

dp[0] = 0
dp[1] = 1

for i in range(2,n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
