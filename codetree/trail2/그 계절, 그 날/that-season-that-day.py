yyyy, mm, dd = map(int, input().split())

#윤년이 아닌 기본 달력 
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]

def isleapYear(y):
    if y%4==0 :
        if y%100 ==0 :
            if y%400==0 :
                return True
            return False
        return True
    return True

def isDay(yyyy,mm,dd):
    #윤년 계산
    if isleapYear(yyyy) :
        month_day[1] = 29
    
    max_month = month_day[mm-1]
    if mm<=12 and max_month >= dd :
        return True
    else :
        return False

def Season(mm) :
    if mm>=3 and mm<=5 :
        return "Spring"
    elif mm>=6 and mm<=8 :
        return "Summer"
    elif mm>=9 and mm<=11 :
        return "Fall"
    elif mm<3 :
        return "Winter"
    else :
        return "Winter"
    
 
if isDay(yyyy,mm,dd) :
    print(Season(mm))
else :
    print("-1")
