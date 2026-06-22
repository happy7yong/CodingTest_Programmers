mm, dd = map(int, input().split())

month_2021 = [31,28,31,30,31,30,31,31,30,31,30,31]

def isDay(mm,dd):
    if mm>12 :
        return False
        
    max_day=month_2021[mm-1]
    if max_day >= dd :
        return True
    return False

if isDay(mm,dd) :
    print("Yes")
else :
    print("No")
    