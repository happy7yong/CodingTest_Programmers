n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x,y= zip(*commands)
# x = []
# dir = []

#배열을 만들기
arr = [[] for _ in range(2*n*max(map(int,x)))]

#현재 위치 초기화
cur = (2*n*max(map(int,x)))//2

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

#흰검회 
answerArr = [0 for i in range(3)]

def isTracking(arr) :
    cntB = 0
    cntW = 0

    for ele in arr :
        if ele == "B" :
            cntB += 1
        elif ele == "W" :
            cntW += 1
    if cntB == 0 and cntW == 0:
        return 0
    elif cntB >= 2 and cntW >= 2:
        return "G"
    elif arr[-1] == "B" :
        return "B"
    elif arr[-1] == "W" :
        return "W"  
    else :
        return 0

for track in arr :
    #회색인지, 검은색인지, 하얀색인지 
    if isTracking(track) == "G" :
        answerArr[2] += 1
    elif isTracking(track) == "B" :
        answerArr[1]+=1
    elif isTracking(track) == "W":
        answerArr[0] +=1

print(" ".join(map(str,answerArr)))








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



