from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [ [False]*m for _ in range(n)]
    dist = [ [0]*m for _ in range(n)]
    
    start = [0,0]
    visited[0][0] = True
    dist[0][0] = 1
    queue = deque([start])
    
    
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    
    while queue :
        curX, curY = queue.popleft()
        
        for i in range(4) :
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            
            if (0 <= nextX < n and 0 <= nextY < m) and not visited[nextX][nextY] and maps[nextX][nextY] == 1:
                visited[nextX][nextY] = True
                dist[nextX][nextY] = dist[curX][curY] + 1
                queue.append([nextX,nextY])
                

    if dist[n-1][m-1] : 
        return dist[n-1][m-1]
    else  :
        return -1
        