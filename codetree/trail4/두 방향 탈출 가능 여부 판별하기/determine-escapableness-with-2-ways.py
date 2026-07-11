n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

curX,curY = 0,0

visited = [[False for _ in range(m)] for i in range(n)]
dx,dy = [0,1],[1,0] # 0: 오른쪽 1: 아래
visited[curX][curY] = True

def in_range(x,y) :
    return (x < n and 0 <= x) and (y < m and 0 <= y)

def dfs(curX,curY):
    for x,y in zip(dx,dy) :
        nextX = curX+x
        nextY = curY+y
        if in_range(nextX,nextY) and not visited[nextX][nextY] and graph[nextX][nextY]==1:
            visited[nextX][nextY] = True
            dfs(nextX,nextY)
            
#우측 하단 도달해야 1
dfs(0,0)
print("1" if visited[n-1][m-1] else "0")
