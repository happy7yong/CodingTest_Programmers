from collections import deque

n, m = map(int, input().split()) #행열 행 n y 열 m x
a = [list(map(int, input().split())) for _ in range(n)]

#문제 유형 : 상하좌우 인접칸 이동, 최단거리 -> BFS
#상태 : x,y 
#반복 조건 : 큐가 있을때, 노드값이 1일때, 
#이동 조건 : 상하좌우 이동
#정답 업데이트 : 그리드 만들어서 최단거리 업데이트

dist = [[0 for _ in range(m)] for i in range(n)]

#visited= [[False for _ in range(m)] for i in range(n)]
startX = 0
startY = 0
q=deque()

dirX,dirY = [1,0,-1,0],[0,-1,0,1]

def in_range(x,y):
    return (x>=0 and m>x) and (y>=0 and n>y)

def bfs(startX,startY) :
    q.append((startX,startY))

    while q :
        curX,curY = q.popleft()

        for dx,dy in zip(dirX,dirY) :
            nx = dx+curX
            ny = dy+curY
            if in_range(nx,ny) and a[ny][nx]==1 and dist[ny][nx]==0 :
                dist[ny][nx] = dist[curY][curX]+1 #업데이트 dist[ny][nx]==0 일때 처음 방문한다는 뜻 
                q.append((nx,ny))


bfs(startX,startY)
print(-1 if dist[n-1][m-1] == 0 else dist[n-1][m-1])