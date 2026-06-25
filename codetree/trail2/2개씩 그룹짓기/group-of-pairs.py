n = int(input())
nums = list(map(int, input().split()))

#2의 배수개의 갯수를 가진 배열
#2개씩 짝지어서 각 그룹의 합 중 최댓값이 최소가 되도록한다. -> 이방법 정렬하고제일큰 값과 제일 작은 값 합치기 하면됬던거같은데
nums.sort()
max_val = 0
left,right = 0, (2*n)-1 
while left < right :
    max_val = max(max_val, nums[left]+nums[right])
    left +=1 
    right -=1 

print(max_val)