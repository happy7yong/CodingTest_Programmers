n, m = map(int, input().split())
MAX_t = 2000000

# 유형: 격자 / 시뮬레이션
# 해야 하는 행동: 첫줄에 4 5로 되어있음.1초에 한칸 씩 좌나 우로 왔다 갔다함.  
# 반복 기준:
# 상태관리: 배열[기준] = 상태 / 배열[시간] = 현재 좌표 위치를 저장 / 현재 상태를 배열에 담아 기억해야됨.
# 제외 기준:
# 정답 갱신: 로봇 A와 B가 다음번에 배열[시간] = 값이 같을때가 몇번인지. 

# Process robot A's movements
t_a = [] #3 5 1 2
d_a = [] #L R L R
for _ in range(n):
    time, direction = input().split()
    t_a.append(int(time))
    d_a.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

#t와 d를 하나하나씩 빼서 배열[시간]=현재 위치 로 상태관리 해야겠음
arrA,arrB = [0] * (MAX_t+1),[0] * (MAX_t+1)

#상태 모두 반영
#이제 각 배열 안에 넣기 배열[시간]=현재위치 
#아 이전 위치를 가져와야하는구나 : 이전 위치 상태를 어떻게 가져오지? 
cur_t_a = 0
for t,d in zip(t_a,d_a) :
    #t는 반복할 횟수를 말하고, d는 움직이는 방향을 뜻한다.
    for _ in range(t) : #t = 3이면 3번 1할꺼임 
        if d == "R" :
            arrA[cur_t_a+1] = arrA[cur_t_a]+1
        elif d == "L" :
            arrA[cur_t_a+1] = arrA[cur_t_a]-1
        cur_t_a+=1

cur_t_b=0
for t,d in zip(t_b,d_b) :
    for _ in range(t) :
        if d == "R" :
            arrB[cur_t_b+1]=arrB[cur_t_b]+1
        elif d == "L" :
            arrB[cur_t_b+1]=arrB[cur_t_b]-1
        cur_t_b+=1

#만약 누군가가 더 많은 시간동안 움직였다면 다른 하나는 배열에 유지해서 저장시켜줘야도미.
max_t = max(cur_t_b,cur_t_a)

for t in range(cur_t_b+1,max_t+1) :
    arrB[t] = arrB[cur_t_b]
for t in range(cur_t_a+1,max_t+1) :
    arrA[t] = arrA[cur_t_a]


cnt=0
#이제 각각의 배열을 탐색하면서 같은 값인 것 카운팅
#근데 이제 시간은 1차원배열이니까. 앞으로만 간답말이지 그래서 길이로 보면됨.
for t in range(1, max(cur_t_a,cur_t_b)+1) :
    if arrA[t] == arrB[t] and arrA[t-1] != arrB[t-1] :
        cnt+=1

print(cnt)
#아 화가난다 너무 못풀어서 졸리니까 더 짜증나고 힘들고 포기하고 싶고 아니 이걸 어캐품 시이발던져버리고 싶네 쉬운거같았는데 이딴것도 생각못하다니 그냥 재능없나봄



#막힌 부분 어떻게 구조를 짜면 알겠는데, 구현을 어떻게 해야할지 모르겠승... 어떻게 코드로 바꿔야하는지 가 어렵더라
#다음번엔 그림으로 그려서 어떻게 넣는지 구상해봐야겠승
#아니 ㅁㅊ 경우의 수 다 따지는게 너무 어려운데 한번의 만남을 어캐 생각해 