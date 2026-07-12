n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y) :
    return x < n

max_cnt = 0

for y in range(n) :
    for x in range(n-3+1) :
        max_cnt = max(max_cnt,grid[y][x]+grid[y][x+1]+grid[y][x+2])

print(max_cnt)