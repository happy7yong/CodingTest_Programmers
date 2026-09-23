n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

#최종적으로 가장 큰 값
max_val = 0

def isRange(y,x) :
    return 0<=y<n and 0<=x<m



#방향
dirArr = [(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#큰 틀에서 중앙값 탐색
#괜히 for 문 들어가서 효율적이게 작성하려고 하지마셈 걍 큰틀안에서 해결한다 생각으로 하기 
for cy in range(n) :
    for cx in range(m) :
        #d1, d2는 방향
        #이번 센터에서 6가지 방향중 가장 큰 합을 찾아봐요
        for d1,d2 in dirArr :
            nd1y=cy+dy[d1]
            nd1x=cx+dx[d1]

            nd2y=cy+dy[d2]
            nd2x=cx+dx[d2]

            if isRange(nd1y,nd1x) and isRange(nd2y,nd2x) and isRange(cy,cx) :


                cur_sum = grid[cy][cx] + grid[nd1y][nd1x] + grid[nd2y][nd2x]
                max_val = max(cur_sum,max_val)

#아 이 핵심 큰틀은 각 중앙에서 6가지 방향으로 다 저장하는거임 따로따로 계산하는게 아니라 결국 관심사가 방향으로 통일되어있으니까 
#한꺼번에 하자 이거지

print(max_val)