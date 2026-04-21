import sys

input = sys.stdin.readline

#플로이드 워샬
#dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
#for k : 중간 섬
# for i : 시작 섬
#  for j :  끝섬

# 버스의 시작 도시 a, 도착 도시 b, 거리 비용 c

#우선 받은걸 위주로 그래프를 그려야됨.


Num_city = int(input())
Bus_Line_Num = int(input())

arr = [[float('INF')]*(Num_city+1) for _ in range(Num_city+1)]

# 자기 자신은 0
for i in range(1, Num_city+1):
    arr[i][i] = 0

for i in range(Bus_Line_Num) :
    s,e,r = map(int,input().split());
    arr[s][e] = min(arr[s][e], r)


for k in range(1, Num_city+1) : 
    for i in range(1, Num_city+1) :
        for j in range(1, Num_city+1) :
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
         
for i in range(1, Num_city+1) :
    for j in range(1, Num_city+1) :
        if arr[i][j] == float('inf') :
             print("0", end=" ")
        else :
            print(arr[i][j], end=" ")
    print()
    
