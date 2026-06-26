n = int(input())
points = [(i,)+tuple(map(int, input().split())) for i in range(1,n+1)]


#번호가 작은 점
points.sort(key=lambda p : (abs(p[1])+abs(p[2]),p[0]))

for point in points :
    print(point[0])



#기존에 있던 배열과 새로만든 배열 두가지를 이용하는 것 


