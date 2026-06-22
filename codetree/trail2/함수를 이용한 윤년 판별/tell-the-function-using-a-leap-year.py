y = int(input())

#윤년 판별 
def is366Years(y) :
    if y%4==0 :
        if y%100==0 and y%400!=0 :
            return False
        return True
    else : 
        return False

if is366Years(y) :
    print("true")
else :
    print("false")