n = int(input())
arr = list(map(int, input().split()))

#완전 탐색 구간별로 모두 확인해야됨.
#구간 2 3 4  -> for 로 돌려서 확인 

cnt=0

def condition(ele, md) :
    return arr[ele] == md

for startIdx in range(n) :
    #구간 별 원소 갯수
    for endIdx in range(startIdx+1,n+1) :
        #모든 원소의 평균값 구하기
        sum=0
        for ele in range(startIdx,endIdx) :
            sum+=arr[ele]
        md = sum/abs(startIdx-endIdx)
        
        for ele in range(startIdx,endIdx) :
            if condition(ele, md) : 
                cnt+=1
                break


print(cnt)