n = int(input())

arr = [[ 0 for i in range(n+1)] for _ in range(n+1)]

#초기값 
for i in range(0,n+1) :
    for j in range(0,i) :
        arr[i][j] = 1

for i in range(1,n+1) :
    for j in range(1, i) :
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

arr = arr[1:n+1:]
for row in arr :
    for ele in row :
        if ele != 0 :
            print(ele,end=" ")
    print()


