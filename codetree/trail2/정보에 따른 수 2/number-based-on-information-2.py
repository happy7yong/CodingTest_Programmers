T, a, b = map(int, input().split())
c = []
x = []

for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

cnt=0
#d1d2찾기
def findD1D2(k) :
    #k에서 가장 가까운 S글자까지의 거리 d1,
    #k에서 가장 가까운 N글자까지의 거리 d2 
    min_S = 1000
    min_N = 1000
    
    for c_c,x_x in zip(c,x) :
        cur_val = abs(k-x_x)
        if c_c == "S" :
            #비교 후 업뎃
            min_S = min(min_S,cur_val)
        elif c_c == "N" :
            min_N = min(min_N,cur_val)
        

    return min_S,min_N


#a<=k<=b

for k_x in range(a,b+1) :
    d1,d2 = findD1D2(k_x) 
    if d1 <= d2 :
        #k_x는 특별한 위치이다.
        cnt+=1

print(cnt)