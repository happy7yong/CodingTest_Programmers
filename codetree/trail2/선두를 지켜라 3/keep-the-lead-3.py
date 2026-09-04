N, M = map(int, input().split())

#상태 : arrA, arrB, fast cnt : 선두 상태가 바뀐 횟수 
#전이 : arrA[t+1] = arrA[t] + v 그러고 arrA를 모두 기록 반복 : zip(v,t) 
#전이 : arrB[t+1] = arrB[t] + v 그러고 arrB를 모두 기록 반복 : zip(v,t) 
#2차 전이 단계 : arrA[t] > arrB[t] -> fast[t] = A
#arrA[t] < arrB[t] -> fast[t] = B
#arrA[t] == arrB[t] -> fast[t] = AB
#정답 갱신 : 반복 : fast, t>1 fast[t] != fast[t-1] -> cnt+=1


v_a = []
t_a = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v_a.append(vi)
    t_a.append(ti)

# Process B's movements
v_b = []
t_b = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v_b.append(vi)
    t_b.append(ti)

arrA = [0]*1000001
arrB = [0]*1000001
#arrA에 시간 당 현재 속도 작성하기 arrA[t] = v
cur_t_a = 0
for vi,ti in zip(v_a,t_a) :
    for _ in range(ti) :
        arrA[cur_t_a+1] = arrA[cur_t_a] + vi
        cur_t_a+=1

cur_t_b = 0
for vi,ti in zip(v_b,t_b) :
    for _ in range(ti) :
        arrB[cur_t_b+1] = arrB[cur_t_b] + vi
        cur_t_b+=1

#몇시간이 가장 최대인지 찾기
max_t = max(cur_t_b,cur_t_a)

fast = [0]*1000001
t= 0
#시간당 선두 주자 : fast배열에 넣기
for av,bv in zip(arrA,arrB) :
    if av>bv : 
        fast[t] = "a"
    elif av<bv :
        fast[t] = "b"
    else :
        fast[t] = "ab"
    t+=1

cnt = 0 
#바뀐 횟수 카운트 반복 : fp : fastplayer 선두주자
for t in range(1,max_t+1) : 
    if fast[t] != fast[t-1] :
        cnt+=1

print(cnt)

