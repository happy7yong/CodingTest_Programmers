n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

sum = 0
max_val = 0
def move(x) :
    return arr[x]
#시작 위치 
for i in range(1,len(arr)) :
    x=i
    sum=0#초기화
    for _ in range(m) :
        cur_x=move(x)#움직임
        sum+=cur_x
        x=cur_x
    #비교 및 업데이트
    max_val = max(sum,max_val)

print(max_val)