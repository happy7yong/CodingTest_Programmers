n, k = map(int, input().split())



arr=[ 0 for i in range(10000+1) ]
for i in range(n) :
    pos, char = input().split()
    if char == "G" :
        pos_num = 1
    else : 
        pos_num = 2
    
    arr[int(pos)] = pos_num


max_sum = 0

for startIdx in range(len(arr)-k) :
    sum=0
    for i in range(startIdx,startIdx+k+1) :
        sum+=arr[i]
    max_sum = max(max_sum,sum)

print(max_sum)

