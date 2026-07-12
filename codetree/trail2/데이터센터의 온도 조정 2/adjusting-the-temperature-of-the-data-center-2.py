n, c, g, h = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
max_scope = max(y for x,y in ranges)

#온도 범위 
#Ta< Tb

max_val = 0

def condition(Ta,Tb,p) :
    if Ta > p :
        return c
    elif p >= Ta and p <= Tb :
        return g
    elif Ta < p :
        return h

#p를 순회하면서 가장 최고의 작업량을 계산해야됨.
for p in range(-1,max_scope+2) :
    sum=0

    for Ta,Tb in ranges :
        sum+=condition(Ta,Tb,p)
    
    max_val=max(sum,max_val)

print(max_val)