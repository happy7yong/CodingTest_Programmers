n = int(input())
arr = list(map(int,input().split()))

min_gap = 100;
#기본적으로 붙어있어야 최솟값임 따라서 붙어있는것만 계산한다
prev_num = 0

for index,ele in enumerate(arr) :
    cur_num = ele
    prev_num = arr[index-1]
    gap = cur_num-prev_num
    if min_gap > gap and gap > 0 :
        min_gap=gap


print(min_gap)
