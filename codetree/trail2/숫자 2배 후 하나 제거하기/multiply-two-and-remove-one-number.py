n = int(input())
arr = list(map(int, input().split()))

# 숫자 2배 후 하나 제거하기 

#인접한 숫자간의 합이 최소가 되도록 한다.

#앞으로 개척해 나가야돼

min_val = 10000

for i in range(n) :
    #2배로 승격
    arr[i]*=2
    
    #선택
    for j in range(n) :
        remaining=[]
        for k,ele in enumerate(arr) :
            if j != k :
                remaining.append(ele)
            
        diff_sum = 0

        #차이 계산하기 
        for k in range(n-2) :
            diff_sum += abs(remaining[k] - remaining[k+1])
        
        min_val = min(diff_sum,min_val)
    arr[i]//=2

print(min_val)
    