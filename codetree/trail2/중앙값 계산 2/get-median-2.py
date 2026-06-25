n = int(input())
arr = list(map(int, input().split()))


for i in range(1,n+1) :
    if i%2!=0:
        cur_arr = sorted(arr[0:i])
        num = i
        print(cur_arr[num//2],end=" ")
    