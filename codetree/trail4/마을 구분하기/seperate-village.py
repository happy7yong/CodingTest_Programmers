n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#방문 처리
visited = [[False for _ in range(n)] for i in range(n)]

dirX,dirY = [1,-1,0,0],[0,0,-1,1]

#상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는것으로 간주


#전체를 탐색할 for문 하나 필요
#그 안에서 dfs를 돌려야됨.
#아이디어 -> dfs확인-> 끊김 for문으로 나감 방문하지 않은 지역이면 Dfs 들어감 
#1은 이웃 지역
p=[]

def grid_in_range(x,y) :
    return (x >= 0 and n > x) and (y >= 0 and n > y)

def in_range(x,y) :
    return (grid[x][y] == 1) and (visited[x][y]==False)

#탐색(동네에 사람 몇명있는지 탐색))
def dfs(curX,curY) :
    global p_cnt
    visited[curX][curY] = True

    for x,y in zip(dirX,dirY) :
        nx = x+curX
        ny = y+curY
        if grid_in_range(nx,ny) and in_range(nx,ny) :

            p_cnt+=1
            dfs(nx,ny)

m_cnt = 0
#동네가 몇명있는지 확인
for y in range(n) :
    for x in range(n) :
        if grid_in_range(x,y) and in_range(x,y) :
            m_cnt +=1
            p_cnt = 1
            dfs(x,y)
            p.append(p_cnt)

p.sort()
print(m_cnt)
print("\n".join(map(str,p)))