n, k = map(int, input().split())
arr = list(map(int, input().split()))

#구간 중 최대 합
#n개의 수들이 주어졌을때, 연속해 k개의 수를 골랐을때, 합이 최대 

max_sum = 0

for startIdx in range(n-k+1) :
    sum=0
    for i in range(startIdx,startIdx+k) :
        sum+=arr[i]
    max_sum = max(max_sum,sum)

print(max_sum)