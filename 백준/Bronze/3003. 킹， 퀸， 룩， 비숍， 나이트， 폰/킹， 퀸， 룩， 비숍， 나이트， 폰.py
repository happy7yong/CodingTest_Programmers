import sys
input = sys.stdin.readline

arr = list(map(int, input().split(" ")))

chase = [1,1,2,2,2,8]
answer = [0 for i in range(6)];

for i in range(6) :
    answer[i] = chase[i] - arr[i];

print(*answer)