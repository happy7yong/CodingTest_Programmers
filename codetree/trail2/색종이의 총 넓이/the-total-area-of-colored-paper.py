n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

offset = 100
cur = offset
total = (100*2)+1

arr = [[0 for _ in range(total)] for i in range(total)]

#points는 좌측 하단 점이 주어진다.

for x,y in points :
    x,y = x+offset, y+offset

    for i in range(x,x+8) :
        for j in range(y,y+8) :
            arr[i][j] = 1

cnt = 0
for row in arr :
    for ele in row :
        if ele == 1 : cnt+=1

print(cnt)


