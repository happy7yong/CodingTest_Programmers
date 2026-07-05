quad = []
quad.append(tuple(map(int,input().split())))
quad.append(tuple(map(int,input().split())))

#A위에 B를 덮었을때 남은 A의 넓이

offset = 1000
triger = True

arr = [[0 for i in range(2*1000+1)] for _ in range(2*1000+1)]


for x1,y1,x2,y2 in quad :
    x1,y1,x2,y2 = offset+int(x1),offset+int(y1),offset+int(x2),offset+int(y2)

    for x in range(x1,x2) :
        for y in range(y1,y2) :
            if triger : arr[x][y] = 1
            else : arr[x][y] = 0

    triger = False

MaxX = -1
MinX = 2001
MaxY = -1
MinY = 2001


for y in range(2*1000+1) :
    for x in range(2*1000+1) :
        if arr[x][y]==1:
            MaxX=max(MaxX,x)
            MinX=min(MinX,x)
            MaxY=max(MaxY,y)
            MinY=min(MinY,y)

if MaxX == -1 :
    print(0)
else :
    X=MaxX-MinX+1
    Y=MaxY-MinY+1
    print(X*Y)
    


