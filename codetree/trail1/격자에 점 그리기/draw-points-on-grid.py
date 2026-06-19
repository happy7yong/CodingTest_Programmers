n,m = map(int,input().split())
#격자 크기 : n
#점의 갯수 : m

number = 1

arr = [[0 for ele in range(n)] for _ in range(n)]

for i in range(m) :
    r,c = map(int,input().split())
    arr[r-1][c-1] = number
    number+=1

print("\n".join(" ".join(map(str,row))for row in arr))
