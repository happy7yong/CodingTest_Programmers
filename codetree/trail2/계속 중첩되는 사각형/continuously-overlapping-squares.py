n = int(input())

offset = 100
max_size = 201

quad = [tuple(map(int, input().split())) for _ in range(n)]

arr = [["" for i in range(max_size)] for _ in range(max_size)]

#사각형 빨 파 빨 파 ...
#땅따먹기 -> 최근 색으로 작성됨.
cnt=0

for x1,y1,x2,y2 in quad :
    x1,y1 = x1+offset,y1+offset
    x2,y2 = x2+offset,y2+offset
    

    for x in range(x1,x2) :
        for y in range(y1,y2) :
            if cnt%2 == 0 :
                arr[x][y] = "R"
            elif cnt%2 != 0 :
                arr[x][y] = "B"
    cnt+=1

blueCnt = 0
for row in arr :
    for ele in row :
        if ele == "B" : blueCnt+=1
    
print(blueCnt)

