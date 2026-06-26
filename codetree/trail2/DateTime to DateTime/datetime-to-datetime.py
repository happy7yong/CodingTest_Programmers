end_day, end_hour, end_mins = map(int, input().split())

cur_day = 11
cur_hour = 11
cur_mins = 11

cnt=0

def isAfterDay(cur_day,cur_hour,cur_mins,end_day,end_hour,end_mins) :
    if (cur_day,cur_hour,cur_mins) > (end_day,end_hour,end_mins) :
        return True
    else : 
        return False

while True :
    if isAfterDay(cur_day,cur_hour,cur_mins,end_day,end_hour,end_mins) :
        cnt = -1
        break

    #종료 조건 : 여기까지 돌리겠음
    if end_day == cur_day and end_hour == cur_hour and end_mins == cur_mins :
        break;

    cnt+=1
    cur_mins+=1

    if cur_mins == 60 :
        cur_hour+=1
        cur_mins=0

    if cur_hour == 24 :
        cur_day+=1
        cur_hour=0
    
print(cnt)