import sys
n = int(input())
nums = list(map(int, input().split()))

# set_nums = set(nums)
# ele_arr = [ele for ele in set_nums]
# dup_arr = []

#이 원소가 중복되지 않아야함 -> 중복인지 확인해야함 -> 갯수를 세기 -> 중복 아니면 최댓값 업데이트
max_val = -1
cnt=0
nums.sort()

for ele in nums :
    if max_val < ele :
        if nums.count(ele) >= 2 :
            continue
        else : max_val = ele
        

    
print(max_val)

