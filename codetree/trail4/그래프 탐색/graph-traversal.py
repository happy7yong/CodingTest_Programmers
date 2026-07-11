n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

#n : 노드의 갯수
#m : 선 갯수 

arr = [[0 for _ in range(n+1)] for i in range(n+1)]

for u,v in edges :
    arr[u][v] = 1
    arr[v][u] = 1

visited = [False for _ in range(n+1)]
visited[1] = True
 
vertex_cnt=0

def dfs(vertex) :
    global vertex_cnt
    for cur_v in range(1,n+1) :
        if arr[cur_v][vertex]==1 and not visited[cur_v] :
            visited[cur_v] = True
            dfs(cur_v)
            vertex_cnt+=1

dfs(1)

print(vertex_cnt)