import sys

input = sys.stdin.readline

#

N,M = map(int,input().split())

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

INF = float('inf')
#간선 리스트
dist = [INF] * (N+1)
dist[1] = 0

# V-1번 반복
for _ in range(N-1) :
    for u, v, w in edges :
        if dist[u] != INF and dist[v] > dist[u] + w : 
            dist[v] = dist[u] + w

# 음수 사이클 체크
for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print(-1)
        exit()

# 출력
for i in range(2, N+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])