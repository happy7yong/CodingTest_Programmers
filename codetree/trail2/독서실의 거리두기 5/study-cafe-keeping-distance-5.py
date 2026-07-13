import sys

n = int(input())
seat = list(map(int,input()))


#최소 거리 측정하기 
def get_arr(arr1) : 
    position = []#값은 1의 위치를 알림

    min_val = sys.maxsize

    for idx,ele in enumerate(arr1) :
        if ele == 1 :
            position.append(idx)
    
    for i in range(len(position)-1) :
        dist = abs(position[i] - position[i+1])
        min_val = min(min_val,dist)
    
    return min_val

ans = 0
        

#자리 마다 1을 모두 넣어서 확인하기
for i in range(n) :
    if seat[i]==0 :
        temp = seat[:]
        temp[i] = 1
    
        min_val=get_arr(temp)
        ans = max(ans,min_val)

print(ans)


    