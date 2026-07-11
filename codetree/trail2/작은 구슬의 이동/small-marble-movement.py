n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

#상하좌우
dirX = [-1,0,0,1]
dirY = [0,1,-1,-0]

#범위
def in_range(x,y) :
    return (x >= 0 and x < n) and (y >= 0 and y < n)

mapping = {
    "U" : 0 ,
    "D" : 3,
    "R" : 1,
    "L" : 2,
}

#초기위치 : r,c
curX,curY = r,c

arr = [ [0 for _ in range(n) ] for i in range(n) ]
#현재 방향 번호
dir_num = mapping[d]
#t초 동안 반복
for _ in range(t) :

    nextX = curX+dirX[dir_num]
    nextY = curY+dirY[dir_num]

    #벽에 부딫치면 반대로 움직인다. -> 범위에 벗어나면 반대로 방향을 바꾼다.
    if in_range(nextX,nextY) :
        #앞으로 전진
        curX+=dirX[dir_num]
        curY+=dirY[dir_num]
    else : 
        #방향 업데이트
        dir_num = 3-dir_num

print(curX+1,curY+1)

    
