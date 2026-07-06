n, m = map(int, input().split())

# def move(time,arr) :
#     cnt = arr[-1]
#     for i in range(time) :
#         cnt+=1
#         arrA.append(cnt)

arrA = []
cnt=0
for _ in range(n):
    direction, time = input().split()
    time = int(time)

    if direction == "R" :
        for i in range(time) :
            cnt+=1
            arrA.append(cnt)
    if direction == "L" :
        for i in range(time) :
            cnt-=1
            arrA.append(cnt)


arrB = []
cnt=0
for _ in range(m):
    direction, time = input().split()
    time = int(time)

    if direction == "R" :
        for i in range(time) :
            cnt+=1
            arrB.append(cnt)
    if direction == "L" :
        for i in range(time) :
            cnt-=1
            arrB.append(cnt)

for i in range(len(arrA)) :
    if arrA[i] == arrB[i] :
        print(i+1)
        break
    if len(arrA)-1 == i : print("-1")

