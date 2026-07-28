#완전탐색
#내가 구하려고 하는것 : cow가 몇번 나오는지 세고 싶다.
#내가 할 수 있는 행동 : 인덱스에 따라 각각 다르게 셀수있는 cow의 가짓수를 센다.
#반복 조건 : for문을 3개를 둔다? 백트래킹이 있는거같은데 
#제외 조건
#사용할 for : 첫번째 c를 찾는 for, 두번째 o를 찾는 for, 세번째 w를 찾는 for 
#정답 갱신 : cnt

#3중 for이라서 성능은 안좋겠지만... 

n=int(input())
arr = list(input())

cnt=0

for c_i in range(n-2) :
    if arr[c_i] == "C" :
        for o_i in range(c_i+1,n-1) :
            if arr[o_i] == "O" :
                for w_i in range(o_i+1,n) :
                    if arr[w_i] == "W" :
                        cnt+=1

print(cnt)