n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

# r, c : startx, starty
#배열을 만듬
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

#arr[행][열] => a[y][x]
curY = r
curX = c

path = []

#우선순위 상하좌우
dirX = [0,0,-1,1]
dirY = [-1,1,0,0]

def range(x,y) :
    return (1 <= x and x < n+1) and (1 <= y and y < n+1)


while True:
    path.append(a[curY][curX])

    moved = False

    for x,y in zip(dirX,dirY):
        dx=curX+x
        dy=curY+y

        if range(dx,dy) and a[curY][curX] < a[dy][dx] :
            curX = dx
            curY = dy
            moved = True
            break

    if not moved :
        break
    

print(*path)