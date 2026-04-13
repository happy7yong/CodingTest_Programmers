import sys
input = sys.stdin.readline

n,m = map(int, input().split())

listenArr = [ input().strip() for _ in range(n)]
WatchArr = [ input().strip() for _ in range(m)]

listenArrS = set(listenArr)
WatchArrS = set(WatchArr)

result = listenArrS & WatchArrS
resultArr = list(result)
resultArr.sort(reverse=False)
Rlength= len(result)
print(str(Rlength)+"\n"+"\n".join(resultArr))