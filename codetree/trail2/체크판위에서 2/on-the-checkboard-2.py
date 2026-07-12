r, c = map(int, input().split())
grid = [list(input().split()) for _ in range(r)]
answer= 0

#시작과 끝 지점은 고정임. (0,0) (r-1,c-1)
#첫번째 중간값 고르기 
for y1 in range(1,r-1) :
    for x1 in range(1,c-1) :
        #시작점과 색이 같으면 점프 불가
        if grid[y1][x1] == grid[0][0] :
            continue
        for y2 in range(y1+1,r-1) :
            for x2 in range(x1+1,c-1) :
                #두번째와 첫번째 색이 같으면 점프 불가
                if grid[y1][x1] == grid[y2][x2] :
                    continue
                #두번째와 end 색 같으면 점프 불가
                if grid[y2][x2] == grid[r-1][c-1] :
                    continue
                answer+=1

print(answer)



