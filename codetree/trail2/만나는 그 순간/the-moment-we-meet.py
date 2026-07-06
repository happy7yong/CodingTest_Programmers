n, m = map(int, input().split())
MAX_T = 1000000

arrA,arrB = [0] * (MAX_T + 1), [0] * (MAX_T+1)
time_a = 1
for _ in range(n):
    direction, time = input().split()
    for _ in range(int(time)) :
        arrA[time_a] = arrA[time_a-1] + (1 if direction == "R" else -1)
        time_a += 1


time_b = 1
for _ in range(m):
    direction, time = input().split()
    for _ in range(int(time)) :
        arrB[time_b] = arrB[time_b-1] + (1 if direction == "R" else -1)
        time_b +=1

ans = -1
for i in range(1,time_a) :
    if arrA[i] == arrB[i] :
        ans = i
        break

print(ans)

