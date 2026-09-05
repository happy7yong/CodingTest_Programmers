n = int(input())
grid = [[0] * n for _ in range(n)]

cur_x = n//2
cur_y = n//2
cur_dist = 1
cur_dir = 1

for_num = 0 

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cur_num = 1 #앞으로 갈때마다 증가
grid[cur_x][cur_y] = cur_num

def in_range(cur_x,cur_y) :
    return cur_x >= 0 and n > cur_x and cur_y >= 0 and n > cur_y

while True :

    
    #한방향으로 전진
    for _ in range(cur_dist):
        #현재 방향으로 앞으로 전진
        cur_x += dx[cur_dir]
        cur_y += dy[cur_dir]
        if not in_range(cur_x,cur_y) :
            break;
        cur_num+=1 #업데이트 
        grid[cur_x][cur_y] = cur_num
    
    for_num+=1
    cur_dir = (cur_dir-1)%4 #움직일 방향 반시방향
    

    if for_num >= 2 :#for_num 2번 후
        cur_dist += 1#거리증가
        for_num = 0#전진 카운트 초기화
    
    if not in_range(cur_x,cur_y) :
            break;
    




for row in grid :
    print(" ".join(map(str,row)))