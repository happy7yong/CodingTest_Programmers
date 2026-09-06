N, S = map(int, input().split())
arr = list(map(int, input().split()))

#상태
sum_val = sum(arr)
min_val = float("inf") #50 - 20 #전체 값에서 기준점을 뺀 값
#i , k : 각각 선택한 값

for i_idx in range(0,N-1) :
    for k_idx in range(i_idx+1,N) :
        #선택한 값을 빼기 
        cur_val = sum_val - (arr[i_idx]+arr[k_idx])
        min_val = min(min_val , abs(S-cur_val))

print(min_val)