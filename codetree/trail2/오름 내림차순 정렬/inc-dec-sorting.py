n = int(input())
nums = list(map(int, input().split()))
nums.sort()
nums_rev = nums[::-1]
print(" ".join(map(str,nums)))
print(" ".join(map(str,nums_rev)))