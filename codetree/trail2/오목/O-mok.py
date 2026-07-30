board = [list(map(int, input().split())) for _ in range(19)]

#내가 뭘 구해야할까요? 유형 : 격자 -> dy,dx
#내가 해야하는 행동 : 한 지점에서 4가지 방향으로 bfs 진행
#반복기준 : 범위 안에 들면 연속으로 확인하기 
#상태관리 : 현재 바둑알 상태
#제외기준 :
#정답갱신 : cnt로 증가
#사용할 for :

#가로 / 세로 / 대각선 위 / 대각선 아래 
dx = [1,0,1,1]
dy = [0,1,-1,1]

cnt_arr = [0,0,0,0] #가로 / 세로 / 대각선 위 / 대각선 아래 
cur_color = 0
ans_color = cur_color
ans_x,ans_y=-1,-1


def is_range(x,y) :
    return (x>=0 and x<19) and (y >= 0 and y < 19)

for c_y in range(19) :
    for c_x in range(19) :
        #각 칸마다 새로 만들어야됨
        cur_color = board[c_y][c_x]

        if board[c_y][c_x] == 0 :
            continue
        

        #4방향 중 하나 
        for idx in range(len(dx)) :
            cnt = 1
            #첫번째 방향은 가로라고 했을때, 4번 반복해서 확인한다.
            for step in range(1,5) :
                nx = c_x+dx[idx]*step
                ny = c_y+dy[idx]*step
                if is_range(nx,ny) and (cur_color == board[ny][nx]) :
                    cnt+=1
            
            if cnt==5 :
                #그 방향으로 2번더해서 중앙값 구하기 
                prev_x = c_x+dx[idx]*2
                prev_y = c_y+dy[idx]*2
                ans_color = cur_color
                ans_y = prev_y
                ans_x = prev_x

print(ans_color)

if ans_color != 0 :
    print(ans_y+1,ans_x+1)