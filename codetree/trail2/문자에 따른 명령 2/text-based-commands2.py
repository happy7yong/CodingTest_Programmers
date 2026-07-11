dirs = input()

#L : 반시계
#R : 시계
#F : 바라보고있는 방향 +1

dx,dy = [1,0,-1,0],[0,1,0,-1]

curX,curY = 0,0

dir_num = 1

for command in dirs :

    #방향 전환만
    if command == "L" :
        dir_num = (dir_num+1)%4

    #방향 전환만
    elif command == "R" :
        dir_num = (dir_num-1+4)%4
    
    #앞으로 이동
    elif command == "F" :
        dir_num = dir_num
        curX,curY = curX+dx[dir_num],curY+dy[dir_num]

print(curX,curY)