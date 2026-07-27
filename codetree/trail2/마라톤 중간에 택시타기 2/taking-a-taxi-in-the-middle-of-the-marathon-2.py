n = int(input())
checkP_arr = [ tuple(map(int,input().split())) for _ in range(n)]

#유형/목적 : 체크포인트 건너뜀> 최소거리
#상태(내가 할 수 있는 행동) : n개의 체크포인트 중 하나만 ㅊ거치지 않는다.
#반복조건 : 하나를 제외한 택시거리로 두 체크포인트의 거리를 계산 
#이동조건 : 체크포인트는 하나씩만 건너뛸수있다. 하나를 제외해야한다. 제외 기준
#정답갱신 : 최소값 갱신
#사용할 템플릿 : 제외할 체크포인트를 하나씩 지정해서 계산에서 제외

min_val = 200000
def MD(p1,p2) :
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

#제외할 체크포인트 0부터 n
for skip in range(1,n-1) :
    #택시거리로 거리 총합 계산
    sum_val = 0
    prev = 0
    for cur in range(1,n) :
        if cur == skip :
            continue
        
        sum_val += MD(checkP_arr[cur],checkP_arr[prev])
        prev = cur
    
    min_val = min(sum_val,min_val)
        
print(min_val)
    
