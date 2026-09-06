N, T = map(int, input().split())
commands = list(input())
board = [list(map(int, input().split())) for _ in range(N)]


#상태
cur_x = N//2 #시작 위치 중앙
cur_y = N//2
cur_dir = 0 #시작방향 북쪽

cnt = board[cur_x][cur_y]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < N

#방향 바꾸기
def change_dir(c, cur_dir) :
    if c == "L" :
        return (cur_dir-1)%4 #현재 위치에서 -1
    elif c == "R" :
        return (cur_dir+1)%4 
    return cur_dir

for c in commands :
    #c가 L R F일때 
    if c != "F" :
        cur_dir = change_dir(c,cur_dir)
    else :
        #앞으로 이동
        next_x = cur_x+dx[cur_dir]
        next_y = cur_y+dy[cur_dir]
        #범위가 아니면
        if not is_range(next_x,next_y) :
            continue
        cur_x=next_x
        cur_y=next_y 
        #현재값 저장
        cnt+=board[cur_x][cur_y]
        

print(cnt)
