m1, d1, m2, d2 = map(int, input().split())
#m1,d1이 기준이 됨 = 월
numsOfMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
daysOfWeek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
daysOfWeekNum = 7

day=0
cnt = 0
if(m1,d1) > (m2,d2) :
    while True :
        if m1==m2 and d1==d2 :
            break
        
        cnt+=1
        
        d1-=1
        if d1 == 0 :
            m1-=1
            d1=numsOfMonth[m1]
    day = -cnt%7

elif (m1,d1) < (m2,d2):
#차이를 계산해야되는데
    while True :
        if m1==m2 and d1==d2 :
            break
        
        cnt+=1
        
        d1+=1
        if numsOfMonth[m1] < d1 :
            d1 = 1
            m1+=1

    day = cnt%7
print(daysOfWeek[day])
    

