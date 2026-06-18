input_arr = [list(map(int,input().split())) for _ in range(4)]
sum=0
for i in range(0,4) :
    for j in range(0,i+1) :
        sum+=input_arr[i][j]
        

print(sum)