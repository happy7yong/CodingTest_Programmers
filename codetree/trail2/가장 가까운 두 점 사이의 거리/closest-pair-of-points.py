n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

#두개의 좌표를 선택해서 제곱의 값을 min으로 덮어쓰기
min_sum = 1000000

for i in range(n) :
    for j in range(i+1,n) :
        x1,y1 = points[i]
        x2,y2 = points[j]

        sum=abs(x2-x1)**2 + abs(y2-y1)**2
        min_sum=min(min_sum,sum)

print(min_sum)