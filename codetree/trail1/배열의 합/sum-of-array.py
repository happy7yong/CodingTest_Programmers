arr_2d = [ list(map(int,input().split())) for _ in range(4)]


for i in range(4) :
    sum=0
    for j in range(4) :
        sum+=arr_2d[i][j]
    print(sum)
        