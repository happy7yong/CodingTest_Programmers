n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_M = n
#좌표가 선택된 상황에서 points위치로 각 사분면에 있는 점 갯수 세기
def geome(x,y) : #x절편 y절편
    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0
    for p_x,p_y in points :
        if p_y < y and p_x > x : #1사 분면
            cnt1+=1
        elif p_y > y and p_x > x :
            cnt2+=1
        elif p_y < y and p_x < x :
            cnt3+=1
        elif p_y > y and p_x < x : 
            cnt4+=1
    
    return cnt1,cnt2,cnt3,cnt4
            
#x=1이 y고 y=1이 x이기때문에, x가 움직이고 있음
for x in range(0,101,2) :#x절편
    for y in range(0,101,2) : #y절편
        m1,m2,m3,m4 = geome(x,y)
        max_val=max(m1,m2,m3,m4)
        min_M = min(max_val,min_M)

print(min_M)