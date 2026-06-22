a, b = map(int, input().split())

#온전수인지 판단하는 함수
def isIntact(i) :
    if i%2!=0 and i%10!=5 and not(i%3==0 and i%9!=0) :
        return True
    return False

#온전수 계산하는 함수
def Intact(a,b) :
    cnt=0

    for i in range(a,b+1) :
        if isIntact(i) :
            cnt+=1
    return cnt


print(Intact(a,b))
