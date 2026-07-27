n = int(input())
room = [int(input()) for _ in range(n)]

#몇명의 사람이 들어가야하는 지 숫자가 적힌 방 존재
#시계반대방향으로 이동
#이웃노드가 존재
#같은 방에서 시작
#구하려는 것 : 각 방이 꽉차는데 걸린 거리 최솟값


#내가 해볼 수 잇는 것 : 시작하는 방을 정하기 
#반복 범위 : n이 다 돌때까지 
#하나 선택 시 바뀌는 것 : 선택한 것부터 cnt 
#반복 조건 : 시계반대방향
#제외 조건
#정답 갱신 : 최솟값 
#for문 구조 : 시작방 start, 

min_val = 1003**100

for startIdx in range(n) :
    sum_val = 0
    cnt=0

    for pIdx in range(startIdx,n+startIdx) :
        pIdx = pIdx%n
        sum_val += cnt*room[pIdx]
        cnt+=1
    
    min_val = min(min_val,sum_val)


print(min_val)