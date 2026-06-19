n,m = map(int,input().split())

#n = 격자 크기 정사각형
#m = 동전의 갯수 / 다음줄부터 나올 라인 수 

arr = [[ 0 for _ in range(n)] for i in range(n)]

for i in range(m) :
    r,c = map(int,input().split())
    for j in range(m) :
        arr[r-1][c-1] = 1

print("\n".join(" ".join(map(str,row)) for row in arr))

