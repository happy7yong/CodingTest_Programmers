from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# 유형 : 격자/상하좌우/도달가능한 칸
# 상태 : visited=[]로 방문상태 x,y / 도달가능한 칸 cnt 
# 반복 기준 : queue가 빌때까지
# 이동기준 : 0일때, 범위안일때, 방문하지 않았을때
# 정답 갱신 : 도달가능하면 cnt+=1
# 사용할 템플릿 BFS

#r행 c열 => y x

q = deque()

cnt = 0

dirX = [0,0,1,-1]
dirY = [1,-1,0,0]

visited = [[False for i in range(n)] for _ in range(n)]

def in_range(x,y) :
    return (x<n and 0<=x) and (y<n and 0<=y)

for startY,startX in points :
    startX-=1
    startY-=1
    q.append((startY,startX))
    visited[startY][startX] = True
    cnt+=1

while q :
    curY,curX = q.popleft()

    for dx,dy in zip(dirX,dirY) :
        nx = dx+curX
        ny = dy+curY
        if in_range(nx,ny) and not visited[ny][nx] and grid[ny][nx] == 0 :
            visited[ny][nx] = True
            q.append((ny,nx))
            cnt+=1

print(cnt)
        




