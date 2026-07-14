from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[ False for i in range(m) ] for _ in range(n)]
visited[0][0] == True

#상하좌우 
dirX = [0,0,1,-1]
dirY = [1,-1,0,0]

def in_range(x,y) :
    return (0 <= x and x < m) and (0<=y and y <n)

def can_go(x,y) :
    return (grid[y][x] == 1) and (visited[y][x]==False)

q = deque()
q.append((0,0))

ans = 0

def bfs() :
    global ans

    while q :
        curX,curY = q.popleft()

        if curX == m-1 and curY == n-1 :
            ans = 1
            break;

        for dx,dy in zip(dirX,dirY) :
            nx = dx+curX
            ny = dy+curY
            if in_range(nx,ny) and can_go(nx,ny) :
                q.append((nx,ny))
                visited[ny][nx] = True
        
bfs()
print(ans)