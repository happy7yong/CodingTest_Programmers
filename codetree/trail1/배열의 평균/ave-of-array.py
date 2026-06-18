arr = [list(map(int,input().split())) for _ in range(2)]

#가로 평균
for i in range(2):
    sum=0
    for j in range(4) :
        sum+=arr[i][j]
    print(round(sum/4,1),end=" ")

#세로 평균
sum=[0 for i in range(4)]
for i in range(2) :
    for j in range(4) :
        sum[j]+=arr[i][j]

print()
sum = [ele/2 for ele in sum]
print(" ".join(map(str,sum)))

#전체 평균
sum=0
for i in range(2) :
    for j in range(4) :
        sum+=arr[i][j]

print(round(sum/8,1))