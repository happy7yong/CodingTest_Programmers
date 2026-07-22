n = int(input())

#2 * dp[i-1] : 마지막 한 열을 1×1 두 개 또는 2×1 하나로 채움
#dp[i-2] : 마지막 두 열을 가로 1×2 두 개로 채움
#part[i]는 i에서 i+1로 넘어가는 행에 걸친 경우 
#->위쪽이 다음 칸으로 튀어나간 상태의 수
#dp는 모두 채운 경우, part는 행에 걸친경우-> 비어있는경우

part = [0]*(n+2)
dp = [0]*(n+2)

part[1]=1
part[2]=3
dp[1] = 2
dp[2] = 7

for i in range(3,n+1) :
    dp[i] =(dp[i-2]+2*dp[i-1]+2*part[i-1])%1_000_000_007
    part[i] = dp[i-1] + part[i-1]

print(dp[n])
