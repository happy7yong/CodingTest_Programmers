n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

#지나간 구역 중 2번 이상 지나간 영역의 크기 ?
offset = 0

#누적합으로 offset 만들기
for i in x :
    offset += i

arr = [0]*offset*2
curX = offset

def walk (start,end) :
    if start > end :
        for i in range(end,start) :
            arr[i]+=1
    else :
        for i in range(start,end) :
            arr[i]+=1
    return end

for i in range(len(x)) :
    if dir[i] == "L" :
        curX = walk(curX,curX-x[i])
    elif dir[i] == "R":
        curX = walk(curX,curX+x[i]) 


cnt=0
for i in arr :
    if i >= 2 :
        cnt+=1
print(cnt)
