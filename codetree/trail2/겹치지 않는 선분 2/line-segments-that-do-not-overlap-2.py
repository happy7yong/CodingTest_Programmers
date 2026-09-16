n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
#어떤 선분과도 교차하지 않는 선분의 수

def isGyocha(a,b,c,d) :#교차하나요?
    return ((a < c) and (b > d)) or ((a > c) and (b < d))


#1. 이번에 선택한 인덱스 
for i in range(0,len(lines)) :
    all = False
    a,b = lines[i]
    for j in range(0,len(lines)) :
        if i==j :
            continue
        c,d = lines[j]
        if isGyocha(a,b,c,d) : #네 교차합니다.
            all = True;
    
    if not all : #교차하지 않는 선분임?
        cnt+=1

print(cnt)


