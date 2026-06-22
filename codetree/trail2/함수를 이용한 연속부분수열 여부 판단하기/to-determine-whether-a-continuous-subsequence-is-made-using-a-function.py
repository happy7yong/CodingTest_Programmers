n_a, n_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#연속인지 판단하는 함수
def isSeq(i_a,n_a,n_b,a,b) :
    if n_b > n_a-i_a : return False
    for i_b in range(n_b) :
        if a[i_a+i_b] != b[i_b] :
            return False
    return True
            
    

#b가 a의 연속부분 수열이냐? 속하냐?
#b의 앞은 무조건 a에 있어야됨 a를 하나씩 확인해보면서 b의 앞과같은지 확인하기
def isContinuSeq(n_a,n_b,a,b) :
    for i_a in range(n_a):
        if a[i_a] == b[0] : #B[0]과 같은 값을 A에서 찾음
            if isSeq(i_a,n_a,n_b,a,b) :#연속인지 확인
                return True
    return False


#속하는지 판단하는 함수 필요
print("Yes" if isContinuSeq(n_a,n_b,a,b) else "No")