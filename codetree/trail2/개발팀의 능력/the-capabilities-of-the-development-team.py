arr = list(map(int, input().split()))

arr.sort()

sum_val = sum(arr)
min_gap = float("INF")
#i 가 기준점이 된다. 
for i in range(0,len(arr)) :
    c_team = arr[i]
    res_val = sum_val - c_team

    for j in range(0,len(arr)) :
        if i == j : continue
        for k in range(0, len(arr)) :
            if i == k : continue
            elif k == j : continue
            a_team = arr[j]+arr[k]
            b_team = res_val - (a_team)

            if a_team == b_team or a_team == c_team or b_team == c_team :
                continue
            min_val = min(c_team,a_team,b_team)
            max_val = max(c_team,a_team,b_team)

            cur_gap = abs(min_val - max_val)
            min_gap = min(cur_gap, min_gap)

if min_gap != float("inf") :
    print(min_gap)
else :
    print("-1")

