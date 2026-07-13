n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]



max_val = 0

for y in range(0,n-3+1) :
    for x in range(0,n-3+1) :
        sum = 0
        for i in range(3) :
            for j in range(3) :
                sum += grid[y+j][x+i]
        max_val = max(sum,max_val)

print(max_val)