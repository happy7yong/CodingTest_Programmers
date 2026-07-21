n = int(input())

#i번째에서 2가지 경우가 잇음 가장 오른쪽이 세로1개/가로2개

dp = [0]*1001

dp[1]=1
dp[2]=2

for i in range(3,n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)



