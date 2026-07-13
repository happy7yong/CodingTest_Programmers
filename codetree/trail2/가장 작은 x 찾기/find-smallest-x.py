n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]


s,e = ranges[0]
#아이디어 모든 경우의 수를 확인해라 
#가능한 모든 조합에 대해 해당 조건에 만족시키는지 확인해라
min_val = 10000

#첫 범위를 시작으로 꺼냄
for s1 in range(0,e+1) :
    cnt=0
    tmp = s1
    for s,e in ranges :
        tmp*=2
        
        if not (s <= tmp and tmp <= e) :
            break
        
        cnt+=1
    
    #모두 도달하고 난 뒤
    if cnt == n :
        min_val = min(min_val,s1)

print(min_val)
        

