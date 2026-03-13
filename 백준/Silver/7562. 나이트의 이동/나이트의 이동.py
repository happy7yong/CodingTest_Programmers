import sys
from collections import deque

input = sys.stdin.readline

t = int(input());


def solution(n, startX, startY, endX, endY):
    queue = deque();
    visited = [[False]*n for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    
    dx = [-2, -2, -1, 1, 2, 2, -1, 1];
    dy = [-1, 1, 2, 2, 1, -1, -2, -2];
    
    queue.append((startX, startY));
    visited[startX][startY] = True;
    
    while(len(queue) != 0) :
        curX, curY = queue.popleft();
        
        for i in range(8) :
            nextX = curX + dx[i];
            nextY = curY + dy[i];
            
            if 0<= nextX < n and 0 <= nextY < n and not visited[nextX][nextY] :
                queue.append((nextX,nextY));
                visited[nextX][nextY] = True;
                dist[nextX][nextY] = dist[curX][curY] + 1
        
    return dist[endX][endY] 
    

for _ in range(t) :
    n = int(input());
    x1, y1 = map(int, input().split(" "));
    x2, y2 = map(int, input().split(" "));
    
    print(solution(n, x1, y1,x2,y2));
    
    
    