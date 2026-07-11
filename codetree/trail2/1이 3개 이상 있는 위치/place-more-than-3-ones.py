n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀있는 칸의 수가 3개이상인 곳 갯수

def in_range(x,y) :
    return (0 <= x and x < n) and (0 <= y and y < n)

dx,dy = [1,0,-1,0],[0,1,0,-1]

ansCnt = 0

for curX in range(n) :
    for curY in range(n) :
        cnt = 0
        
        for dirX,dirY in zip(dx,dy) :
            x = curX+dirX
            y = curY+dirY
            if in_range(x,y) and grid[x][y] == 1 :
                cnt+=1
        
        if cnt>=3 : ansCnt+=1

print(ansCnt)