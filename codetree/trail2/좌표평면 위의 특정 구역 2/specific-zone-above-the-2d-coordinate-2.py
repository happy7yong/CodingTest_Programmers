n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

#하나의 점만 빼서 -> 하나씩 모두 순회하며 특정일 경우 
#각 점의 최대 최소 구하기 x버전의 최대 최소, y버전의 최대 최소를 구해서 각 뺀다음 곱하기
min_weight=1600000000
#i는 특정 값 고르기
for i in range(n) :
    #순회하며 배열에 넣을 값 선택하기 
    maxX = 0
    minX = 40000
    maxY = 0
    minY = 40000
    for j in range(n) :
        if i == j :
            continue
        
        x,y=points[j]
        minX=min(minX,x)
        maxX=max(maxX,x)
        minY=min(minY,y)
        maxY=max(maxY,y)
    
    w=abs(minX-maxX)
    h=abs(minY-maxY)
    #최솟값 구하기 
    min_weight = min(min_weight,w*h)

print(min_weight)

        
