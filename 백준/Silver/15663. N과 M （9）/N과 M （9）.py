import sys
input = sys.stdin.readline

N,M = map(int,input().split(" "))

arr = list(map(int,input().split(" ")))
arr.sort()


curArr = [];
answer = [];
visited = [False] * N

def solution(depth):
    if depth == M:
        print(*curArr)
        return
    
    prev = -1
    
    for i in range(N):
        if visited[i]:
            continue
        
        if arr[i] == prev:
            continue
        
        visited[i] = True
        curArr.append(arr[i])
        
        solution(depth + 1)
        
        curArr.pop()
        visited[i] = False
        prev = arr[i]

solution(0)
print("\n".join(" ".join(map(str, a)) for a in answer))