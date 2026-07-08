from collections import deque

n, k = map(int, input().split())

que = deque()

#6번 반복으로 큐에 사람 넣기
#k번 popleft로 밀어내기
#빌때까지 반복

answer = []

for i in range(n) :
    que.append(i+1)


while len(que) != 0 :
    for _ in range(k-1) :
        que.append(que[0])
        que.popleft()
    answer.append(que.popleft())

print(" ".join(map(str,answer)))