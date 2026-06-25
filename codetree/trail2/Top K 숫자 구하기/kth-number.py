n, k = map(int, input().split())
nums = list(map(int, input().split()))

#n : 원소의 갯수 | k : 구하려는 수

nums.sort()
print(nums[k-1])