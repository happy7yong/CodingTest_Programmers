n = int(input())

dx,dy = [1,0,-1,0],[0,1,0,-1]

#W서 S남 N북 E동

curX,curY = 0,0

for _ in range(n) :
    dir,dist = input().split()
    dist = int(dist)
    
    if dir == "W" :
        curX = curX+dx[2]*dist
        curY = curY+dy[2]*dist
    elif dir == "S" :
        curX = curX + dx[3]*dist
        curY = curY + dy[3]*dist
    elif dir == "N" :
        curX = curX + dx[1]*dist
        curY = curY + dy[1]*dist
    elif dir == "E" :
        curX = curX + dx[0]*dist
        curY = curY + dy[0]*dist

print(curX,curY)