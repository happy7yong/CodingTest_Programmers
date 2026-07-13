n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


#3개씩 끊겨져 있고 회전할 수 있음. 
#시계방향으로 이동

def move() :
    tempu=u[-1]
    tempd=d[-1]
    
    for i in range(n-1,0,-1) :
        d[i]=d[i-1]
        u[i]=u[i-1]
        
    d[0] = tempu
    u[0] = tempd
    
        

#t초만큼 이동
for i in range(t) :
    #각각 이동시킴
    move()

print(" ".join(map(str,u)))
print(" ".join(map(str,d)))