N, B = map(int, input().split())
p = [int(input()) for _ in range(N)]

max_val = 0
#할인 받을 학생 선택
for i in range(0,len(p)) :
    p_c=p[:]
    p_c[i] = p[i]//2

    p_c.sort()
    sum = 0
    cnt = 0

    for k in p_c :
        if sum+k <= B :
            sum+=k
            cnt+=1
        elif sum+k > B :
            break
    
    #max
    max_val = max(cnt,max_val)

print(max_val)
