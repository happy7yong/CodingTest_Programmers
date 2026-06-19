n,m = map(int,input().split())

arr = [[0 for i in range(n)] for _ in range(n)]

for i in range(m) :
    r,c = map(int,input().split())
    arr[r-1][c-1] = r*c

print("\n".join(" ".join(map(str,row)) for row in arr))