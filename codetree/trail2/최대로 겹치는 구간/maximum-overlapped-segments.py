n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
max_val=0
min_val=100
#최댓값 찾기
for s,e in segments :
    if min_val > min(s,e) :
        min_val = min(s,e)

    if max_val < max(s,e) :
        max_val = max(s,e)

offset = abs(min_val) if min_val < 0 else 0
total = offset + max_val + 1
arr = [0]*(total)

for s,e in segments :
    for i in range(offset+s,offset+e) :
        arr[i] +=1
    

print(max(arr))
