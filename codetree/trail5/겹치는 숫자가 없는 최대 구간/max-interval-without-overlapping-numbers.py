n = int(input())
arr = list(map(int, input().split()))


left = 0

each = [0]*100001

max_dist = 0

#중복되는 숫자가 전혀 없는 경우

#겹치는 숫자가 없는 최대 구간
for right in range(n) :
    each[arr[right]]+=1

    while each[arr[right]]>=2 :
        each[arr[left]] -=1 
        left+=1
    
    max_dist = max(max_dist,right-left+1)

print(max_dist)

    