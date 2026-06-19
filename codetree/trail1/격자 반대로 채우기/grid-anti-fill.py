n=int(input())

arr = [[0 for _ in range(n)] for i in range(n)]
cnt = n*n

if n%2==0 :
    for i in range(n) :
        if i%2==0 : #짝수 -> 아래로 
            for j in range(n-1,-1,-1):
                arr[j][i] = cnt
                cnt -=1
        else : #홀수 -> 위로 
            for j in range(n) :
                arr[j][i] = cnt 
                cnt -=1
else : 
    for i in range(n) :
        if i%2==0 : #짝수 -> 아래로 
            for j in range(n):
                arr[j][i] = cnt
                cnt -=1
        else : #홀수 -> 위로 
            for j in range(n-1,-1,-1) :
                arr[j][i] = cnt 
                cnt -=1
print("\n".join(" ".join(map(str,ele)) for ele in arr))
