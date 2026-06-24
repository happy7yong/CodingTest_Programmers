n = int(input())
arr = list(map(int, input().split()))
max=0

def f(depth,max,arr) :
    #n까지 들어왔을때 최댓값
    if max <= arr[depth]:
        max = arr[depth] 

    if depth<=0 :
        return max
    
    return f(depth-1,max,arr) #현재 최솟값도 같이 return 

print(f(n-1,max,arr))