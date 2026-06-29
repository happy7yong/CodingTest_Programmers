n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

max_val = 0

for s,e in segments :
    if max_val < max(s,e) :
        max_val = max(s,e)

arr = [0]*(max_val+1) #헷갈리지 않게 0은 사용하지 않음

for s,e in segments :
    for i in range(s,e+1) :
        arr[i] +=1

print(max(arr))