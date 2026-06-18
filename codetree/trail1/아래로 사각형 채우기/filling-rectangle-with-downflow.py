n = int(input())

arr = [[ 1 for j in range(n)] for i in range(n+1)]

for i in range(1,n+1) :
    for j in range(n) :
        arr[i][j] = i+j*n

arr = arr[1:n+1:]
print("\n".join(" ".join(map(str,row)) for row in arr))