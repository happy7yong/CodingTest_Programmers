n = int(input())
a, b, c = map(int, input().split())
c_arr = [a,b,c]
cur_arr = []

arr = [0 for _ in range(n)]
cnt=0

#n은 수의 갯수
#1 2 3은 조합

#cur_arr : 현재 조합 c_arr : 제시해준 조합
#i : 현재 인덱스
def condition(cur_arr,i) :
    return abs(c_arr[i]-cur_arr[i]) <= 2

#3개의 튜플 조합
for i in range(1,n+1) :
    cur_arr.append(i)
    for j in range(1,n+1) :
        cur_arr.append(j)
        for k in range(1,n+1) :
            cur_arr.append(k)
            for idx in range(3) :
                if condition(cur_arr,idx) :
                    cnt+=1
                    break
            cur_arr.pop()
        cur_arr.pop()
    cur_arr.pop()

print(cnt)
