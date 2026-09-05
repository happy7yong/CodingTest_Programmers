N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]


dir_num = {
    "N" : 0, #북 -1,0
    "E" : 1, #동 0,1
    "S" : 2, #남 1,0
    "W" : 3, #서 0,-1
}

#방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cur_x = 0
cur_y = 0
cur_d = 0

cnt=0
ans = -1

for dr,ds in zip(dir,dist) :
    for _ in range(ds) :
        cur_x = cur_x+dx[dir_num[dr]]
        cur_y = cur_y+dy[dir_num[dr]]
        cnt+=1
        if cur_x == 0 and cur_y == 0 :
            ans = cnt 
            break;
    if ans != -1 :
        break  

print(ans)