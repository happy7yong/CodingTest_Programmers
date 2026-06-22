a, b = map(int, input().split())

cnt=0

#모든 자릿수의 합이 짝수인 수 구하는 함수
def isSumF(i):
    sum_val = sum(map(int,list(str(i))))
    if sum_val%2==0:
        return True
    else :
        return False

#소수
def isMinority(i) :
    for ele in range(2,i) :
        if i%ele==0 :
            return False
    
    return True

for i in range(a,b+1) :
    if isMinority(i) and isSumF(i) :
        cnt+=1

print(cnt)