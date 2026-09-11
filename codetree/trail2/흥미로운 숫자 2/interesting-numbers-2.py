x, y = map(int, input().split())

#흥미로운 숫자 카운팅
cnt = 0

def isInteresting(n) :
    arr = [0]*10
    vnt=0
    v_1 = False
    #각 자릿수를 각각 숫자로 구분 한다.
    #숫자로 변환한다음 배열에 자릿수 저장
    for i in list(map(int,list(str(n)))):
        arr[i] += 1
    
    #배열확인 : 0이 아닌 인덱스가 2개고, 한값이 1일때 return True
    for i,v in enumerate(arr) :
        if v != 0 :
            vnt +=1
        if v == 1 :
            v_1 = True
    
    return vnt == 2 and v_1
            



for i in range(x,y+1) :
    if isInteresting(i) :
        cnt+=1
    
print(cnt)