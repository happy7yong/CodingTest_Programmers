n,m = map(int,input().split())
num=0
arr = [[0 for ele in range(m)] for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        num+=1
        arr[i][j]=num


print("\n".join( " ".join(map(str,row)) for row in arr))