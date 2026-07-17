from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dirX = [1, -1, 2, -2, 2, -2, 1, -1]
dirY = [-2, -2, -1, -1, 1, 1, 2, 2]

dist = [[-1 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

q = deque()

def bfs(startX, startY):
    q.append((startX, startY))
    dist[startY][startX] = 0

    while q:
        curX, curY = q.popleft()

        for dx, dy in zip(dirX, dirY):
            nx = curX + dx
            ny = curY + dy

            if in_range(nx, ny) and dist[ny][nx] == -1:
                dist[ny][nx] = dist[curY][curX] + 1
                q.append((nx, ny))

bfs(c1 - 1, r1 - 1)

print(dist[r2 - 1][c2 - 1])