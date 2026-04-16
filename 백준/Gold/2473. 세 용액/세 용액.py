import sys

input = sys.stdin.readline

#구간합

#다 합친 값을 0으로 만들 것이다.
#주어진 용액들의 특성값이 [-2, 6, -97, -6, 98]인 경우에는 
#특성값이 -97와 -2인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 
#이 용액이 특성값이 0에 가장 가까운 용액이다.
#세 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액

#투포인터 처럼 양끝점을 잡고 시작?

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

min_v = float('inf');
answer = [0,0,0];

#0에 더 가까운걸 어떻게 인식시키지?
#0에서 뺏 절댓값의 수가 낮을때 

#투포인터
#1. 배열 정렬
#2. 하나 고정 (i)
#3. 나머지 두 개는 투포인터 (left, right)
#그림으로
# [-2 -1 0 1 2 ]
#  i  L      R

#정렬하면
#합이 크면 → right 줄임
#합이 작으면 → left 늘림


for fix_index in range(n-2) :
    left_index = fix_index+1
    right_index = n-1
    
    #해당 fix_index를 지정하고 모두 탐색하고 넘어가야됨.
    while left_index < right_index :
        value = arr[fix_index] + arr[left_index] + arr[right_index]
        
        if abs(value) < min_v:
            min_v = abs(value)
            answer = [arr[fix_index], arr[left_index], arr[right_index]]
    
        if value > 0 :
            #다 더한 값이 0보다 클경우엔 right를 --
            right_index-=1;
        else :
            #다 더한 값이 0보다 작을 경우엔 더 증가시켜야됨.
            left_index+=1
    
            

print(*answer)
