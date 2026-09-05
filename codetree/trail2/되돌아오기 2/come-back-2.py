commands = input()
coms = list(commands)

#방향 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


#상태 
cur_x = 0
cur_y = 0
cur_dir = 0

def change_dir(c,cur_dir) :
    if c == "R" :
        return (cur_dir-1)%4
    elif c == "L" :
        return (cur_dir+1)%4

cnt=0     
ans = -1 

for c in coms :
    if "F" != c :
        cur_dir = change_dir(c,cur_dir)
    else :
        cur_x+=dx[cur_dir]
        cur_y+=dy[cur_dir]
    cnt+=1
    
    if cur_x ==0 and cur_y == 0:
        ans = cnt
        break


print(ans)
