n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)] #움직일 좌표

#상태 : 현재위치 / 배열 arr / dx,dy / 각 배열의 방문상태 visited = boolean /현재 방향d
#전이 : d = 0 이고 4로 항상 나눔
#전이 : 방향 바뀌면 dx[(d+1)%4]
#전이 : 다음 좌표로 이동 next_x = cur_x[]
#2차 전이 : in_range(cur_x,cur_y) and in_visited()
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#상태 : 현재 위치
cur_x = 0
cur_y = 0

#상태 : 현재 방향
d = 0
#앞으로 전진할 경우사용 방법 : cur_x+dx[d] cur_y+dy[d]

visited = [[False] * m for _ in range(n)]

cnt=1
arr[cur_x][cur_y] = cnt
visited[cur_x][cur_y] = True

def in_range(x,y) :
    return (x>=0 and x<n) and (y>=0 and y<m)

while cnt < n*m:
    #앞으로 전진하면서 숫자 카운팅
    next_x = cur_x+dx[d]
    next_y = cur_y+dy[d]
    #앞으로 갈수있나?
    if in_range(next_x,next_y) and not visited[next_x][next_y] :
        cur_x=next_x
        cur_y=next_y

        cnt+=1
        arr[cur_x][cur_y] = cnt
        visited[cur_x][cur_y] = True
    else :
        #방향 바꾸고 발도장
        d = (d+1)%4

for row in arr : 
        print(" ".join(map(str,row)))
    

