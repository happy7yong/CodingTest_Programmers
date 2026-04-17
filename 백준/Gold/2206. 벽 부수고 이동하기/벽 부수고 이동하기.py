import sys
from collections import deque
input = sys.stdin.readline

#벽을 부수고도 최단거리가 나온다면 벽을 부숴도된다..? 그럼 다 부셔봐야되는거아님? 벽을 부수는 기준이 있을꺼아니야
#벽을 부수는 기준은 없다. 가능하면 다 해본다 가 핵심
#완전탐색이 아니라 이것도 그래프 탐색이다. 짧은 거리부터 
#dist는 벽을 한 번 부술 수 있는 상태를 포함해서 최단거리 BFS를 한다
#기존 (x,y) => (x,y,broken)
#BFS는 단방향이 아니라 옆으로 계속 퍼지면서 이동한다. 감염(확산)의 느낌이 맞다.
#그럼 만약 dist[nextX][nextY]가 현재 거리보다 크면 현재 거리를 넣는 로직도 들어가야되나? 
# -> 오해다. 애초에 dist에 처음 들어간 값일 경우가 최단거리이다. 때문에 말자체가 성립되지 않는다.

#아 그러니까 4갈래 길로 만들어지고 BFS는 하나의 직선이 시간선이라고 할때 여러 평행세계가 생겨나는구나. 분기분기분기 가 모두 다르기 때문에
#한방향이 아니라 여러 직선에서 만들어지는 것을 BFS라고 하는 구나. 이걸 이용해서 한 직선에서는 벽한번만 부술수있으니까...와우

#(상태 관리 차원에서 각각 요소가 두가지 상태를 갖고 있음.)벽을 부순 경우 : [False]*2 는 하나의 요소에 두가지 상태를 갖고 있음을 나타냄.


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def bfs():
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    dist = [[[0]*2 for _ in range(m)] for _ in range(n)]

    queue = deque([(0,0,0)])
    visited[0][0][0] = True
    dist[0][0][0] = 1

    while queue:
        x, y, broken = queue.popleft()

        if x == n-1 and y == m-1:
            return dist[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 길
                if arr[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    dist[nx][ny][broken] = dist[x][y][broken] + 1
                    queue.append((nx, ny, broken))

                # 벽
                if arr[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    dist[nx][ny][1] = dist[x][y][0] + 1
                    queue.append((nx, ny, 1))

    return -1

print(bfs())