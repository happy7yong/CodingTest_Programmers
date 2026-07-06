n = int(input())
arr = [int(input()) for _ in range(n)]

#부호가 동일한 정수로만 이루어졌을때 연속 부분 수열이라고 함.
# 0보다 큰 경우가 연속될 경우, 0보다 작은 경우가 연속될 경우
#한번 부호가 바뀌면 그 부호로 on 되어있어야됨.
#앞에있는 부호가 같을때 cnt 증가
#앞에 있는 부호가 같은지 알려면 -2 -3 -> abs()로 나눈 값이 같을때, cnt 증가

max_cnt = 1
cnt = 1

for i in range(n) :
    if i > 0 and arr[i]//abs(arr[i]) == arr[i-1]//abs(arr[i-1]) :
        cnt+=1
    else :
        cnt=1
    
    max_cnt = max(max_cnt,cnt)

print(max_cnt)