n, m = map(int, input().split())

MAX_V = 1000000

arrA = [0] * 1000001

cur_time = 1
for i in range(n) :
    v,t = map(int,input().split())
    for _ in range(t) :
        arrA[cur_time] = arrA[cur_time-1] + v
        cur_time+=1

arrB = [0] * 1000001

cur_time = 1
for i in range(m) :
    v,t = map(int,input().split())
    for t_val in range(t) :
        arrB[cur_time] = arrB[cur_time-1] + v
        cur_time+=1

#선두가 바뀌다.
#그 전에 누가 있었는지 기억해야됨.
#A였다면  
cnt = -1
pri = ""
for i in range(cur_time) :
    if arrA[i] > arrB[i] :
        if pri != "A" :
            cnt+=1
        pri = "A"
    elif arrA[i] < arrB[i] :
        if pri != "B" :
            cnt+=1
        pri = "B"
    
print(cnt)