import sys

n = int(input())
arr = list(map(int, input().split()))

#한곳에 모두 모이려고 한다. 적절한 집에 선택해 모든 사람들의 이동거리의 합 최소

#이동거리 합 최소

sum = 0
min_val = sys.maxsize

#완전 탐색 
for curIdx in range(n) :
    #나의 idx에서 현재 idx를 빼기
    sum=0
    for idx,p_n in enumerate(arr) :
        sum+=p_n*(abs(idx-curIdx))
    min_val = min(sum,min_val)

print(min_val)
