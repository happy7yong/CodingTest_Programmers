import sys

input = sys.stdin.readline

n = int(input())


def function() :
    if n==1 : return 1
    if n==2 : return 3
    if n==0 : return 0
    
    
    dp = [0 for _ in range(n+1)]
    
    dp[1] = 1
    dp[2] = 3
    dp[0] = 0

    
    for i in range(3,n+1) :
        dp[i] = 2*dp[i-2] + dp[i-1]
    
    return dp[n]%10007
    

print(function());