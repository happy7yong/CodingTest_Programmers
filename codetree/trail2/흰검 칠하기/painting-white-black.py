n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x,y= zip(*commands)

total = sum(map(int,x))

#배열을 만들기
arr = [[] for _ in range(2*(total+1))]

#현재 위치 초기화
cur = total//2

def Ldraw(arr,num,cur) :
    #왼쪽으로 갈경우
    for i in range(cur,cur-num,-1) :
        arr[i].append("W")

    return cur-num+1

def Rdraw(arr,num,cur) :
    #오른쪽으로 갈경우
    for i in range(cur,cur+num) :
        arr[i].append("B")

    return cur+num-1

for num, direction in commands:
    num = int(num)
    # x.append(int(num))
    # dir.append(direction)
    if direction == "R" :
        cur = Rdraw(arr,num,cur)
    else : 
        cur = Ldraw(arr,num,cur)


def isTracking(arr) :
    cnt_B = arr.count("B")
    cnt_W = arr.count("W")

    if cnt_B >= 2 and cnt_W >= 2 :
        return "G"
    elif not arr :
        return 0
    else :
        return arr[-1]

w = 0
b = 0
g = 0

for track in arr :
    result = isTracking(track)
    #회색인지, 검은색인지, 하얀색인지 
    if result == "G" :
        g += 1
    elif result == "B" :
        b+=1
    elif result == "W":
        w +=1

print(w,b,g)








#왼쪽 오른쪽으로만 움직이는 게 
#왼쪽으로가면 흰색만 칠하고 
#오른쪽으로가면 검은색만 칠한다.
#주의 : 흰색 검은색 각각 두번 이상 칠해지면 회색으로 바뀐다. 
# 흰2 검2일경우 회색으로 바뀜 -> 회색 검은색 추적해야됨. 
#시뮬레이션 구간칠하기 배열에서 1을 찍었었기 때문에 
#2차원으로 정리할 것.
#[[],[],[]] 으로 정리하는데, 2차원배열으로 정리해야할 것.
#마지막에 WB 갯수 count해서 정리
#arr[i].append(W or B)를 넣기



