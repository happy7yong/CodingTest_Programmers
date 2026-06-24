n = int(input())
arr = list(map(int, input().split()))

def f(d) :
    #n까지 들어왔을때 최댓값
    if d==0 :
        return arr[d]

    return max(f(d-1), arr[d])


print(f(n-1))