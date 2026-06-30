n = int(input())
x1, y1, x2, y2 = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

#오프셋 구하기
offsetX = abs(min(x1+x2))
offsetY = abs(min(y1+y2))

arrXMax=offsetX+max(x1+x2)
arrYMax=offsetY+max(y1+y2)

x1 = [offsetX+ele for ele in x1]
x2 = [offsetX+ele for ele in x2]
y1 = [offsetY+ele for ele in y1]
y2 = [offsetY+ele for ele in y2]

#2차 좌표 만들기
arr = [[0 for _ in range(arrXMax)] for i in range(arrYMax) ]

#사각형을 구하는 공식 : abs(x1-x2) * abs(x1-y2)
#사각형 칠하기 : 첫번째 사각형 칠하기
sum=0
for idx in range(n) :
    for y in range(y1[idx],y2[idx]) :
        for x in range(x1[idx],x2[idx]) :
            if arr[y][x] < 1 :
                arr[y][x] = 1

cnt=0
for col in arr :
    for ele in col :
        if ele == 1 :
            cnt+=1 

print(cnt)