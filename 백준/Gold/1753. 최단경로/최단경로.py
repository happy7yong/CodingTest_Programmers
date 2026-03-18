import heapq, sys

input = sys.stdin.readline

V,E = map(int,input().split(" "))

start = int(input());

arr = [list(map(int,input().split(" "))) for _ in range(E)]
graph = [[] for _ in range(V+1)];

for u, v, w in arr:
    graph[u].append((w,v))

# print(graph)


def dijkstra():
    #dist
    #heapq
    #visited
    #방향벡터
    
    dist = [float('INF')]*(V+1); #i까지의 거리  
    dist[start] = 0
    
    heap = []; #“이미 계산된 거리들 중에서 가장 짧은 것”을 뽑는 역할
    heapq.heappush(heap, (0,start)); #0은 지금까지 쌓아온 dist라는 뜻. 
    
    while heap:
        curDist,curNode = heapq.heappop(heap);
        
        if dist[curNode] < curDist : continue
        
        for cost,nextNode in graph[curNode] :
            if dist[nextNode] > curDist + cost :
                
                dist[nextNode] = curDist + cost
                heapq.heappush(heap, (curDist + cost,nextNode))


    
    return "\n".join("INF" if d == float('inf') else str(d) for d in dist[1:])


print(dijkstra())