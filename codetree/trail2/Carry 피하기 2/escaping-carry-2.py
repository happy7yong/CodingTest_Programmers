#내가 구하려고 하는 것 : 3개를 골랐을때 carry가 발생하지 않을 수 있는 합의 최댓값
#carry : 10의 자리를 넘기는 것 
#내가 해야하는 행동 : 수를 더했을때 기존 수의 갯수와 달라지지 않았을 경위 최댓값 갱신
#반복기준 : n의 자리를 더했을때 n+1에 위치한 수가 달라지는지 확인한다.
#제외기준
#사용할 for 
#정답 갱신 : 최댓값 갱신

n = int(input())
arr = [int(input()) for i in range(n)]

max_val = -1

def isCarry(a,b,c) :
    #한자리씩 보고 싶을 경우는 10으로 나눈 나눗셈으로 확인한다.
    while a>0 or b>0 or c>0 :
        if a%10 + b%10 + c%10 >= 10 :
            return True
        
        a//=10
        b//=10
        c//=10
    
    return False




for i in range(n) :
    for j in range(i+1,n) :
        for k in range(j+1,n) :
            if not isCarry(arr[i],arr[j],arr[k]) : #carry가 발생하지 않았을 때
                sum = arr[i]+arr[j]+arr[k]
                max_val = max(sum,max_val)

print(max_val)