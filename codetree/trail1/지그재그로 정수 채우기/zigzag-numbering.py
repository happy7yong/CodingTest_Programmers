n, m = map(int, input().split())

arr = [[0 for i in range(m)]for _ in range(n)]
cnt=0
for i in range(m) :
    for j in range(n) :
        if i%2==0 : #짝수
            arr[j][i] = cnt 
        else : #홀수
            arr[n-j-1][i] = cnt
        cnt+=1


print("\n".join(" ".join(map(str,row)) for row in arr))
