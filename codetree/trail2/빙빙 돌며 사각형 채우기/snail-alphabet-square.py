n, m = map(int, input().split())
grid = [[0]*m for _ in range(n)]

#알파벳 순서
ar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
#현재 알파벳 넘버 상태
alpha_n = 0
#현재 알파벳
cur_ar = ar[alpha_n]

cur_x = 0
cur_y = 0
cur_dir = 1
# cur_rc = 0 # 현재 부분이 가로인지 세로인지 기억하는 상태
# cur_dist = n #현재 직선으로 가야하는 길이

dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[False]*m for _ in range(n)]
grid[cur_x][cur_y] = cur_ar
visited[cur_x][cur_y] = True

def is_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y<m

#빙빙도는 반복 조건 : ar의 길이보다 현재 알파벳 넘버가 더 클때
while True :#True 인 동안에 반복
    #직선 반복 조건 : 앞에 범위에 벗어나거나 이미 방문했을 경우 방향 전환
    
    #앞에 예측
    next_x = cur_x + dx[cur_dir]
    next_y = cur_y + dy[cur_dir]
    #앞으로 못가면
    if not is_range(next_x,next_y) or visited[next_x][next_y] :
        #방향 전환
        cur_dir = (cur_dir+1)%4
    
    cur_x +=dx[cur_dir]
    cur_y +=dy[cur_dir]
    if not is_range(cur_x,cur_y) or visited[cur_x][cur_y] :
        break;

    #알파벳 넘버 증가
    alpha_n = (alpha_n+1)%len(ar)
    cur_ar=ar[alpha_n]#넘버가 가리키는 진짜 알파벳
    grid[cur_x][cur_y] = cur_ar #발자국 남김
    visited[cur_x][cur_y] = True

for row in grid :
    print(" ".join(map(str,row)))

