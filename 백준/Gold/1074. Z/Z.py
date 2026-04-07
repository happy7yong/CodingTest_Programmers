import sys

input = sys.stdin.readline

n,r,c = map(int,input().split(" "))
#r : 3  c : 1

#2*n은 전체 배열의 크기다.
sizeXN = 2**n
sizeYN = 2**n

startX = 0;
startY = 0;
endX = sizeXN;
endY = sizeYN;

    
#분할 정복을 사용하기 위해선 반복구간을 찾아야됨.
#어떤 함수에 들어갔을때 항상 오른쪽 > 대각선 > 오른쪽으로 움직인다. 총 4번 탐색
#어떤 함수 시작배열은 항상 2의 지수 인덱스임 2 4 8 
#첫번째 이동 [0][0] / [2][] / [][2] / [2][2]
#0,0 / 0,1 / 1,0 / 1,1
#0,2 / 0,3 / 1,2 / 1,3
#한덩이를 받으면 4등분한다.

# 배열 만들어서 탐색 → 시간 터짐
# 내가 찾는 좌표가 몇 번째인지 계산
# 현재 (r, c)가 어디 사분면인지 판단하고
# 그 전에 지나간 칸 개수를 더함
# 모두 그걸 돌필욘없이 내가 있는 그룹에서 몇번째인지만 알면되는구나 뭔가 정석대로 않풀어도 ㅋㅎㅋㅊㅋ 


def funZ(startX, endX, startY, endY) :
    midX = (startX + endX)//2
    midY = (startY + endY)//2 
    size = midX - startX
    
    if startX+1==endX and startY+1==endY : 
        return 0;
    
    if c < midX and r < midY : #1사
        return funZ(startX, midX, startY, midY)
    elif c >= midX and r < midY : #2사
        return size*size + funZ(midX, endX, startY, midY)
    elif c < midX and r >= midY : #3사
        return size*size*2 + funZ(startX, midX, midY, endY)
    elif c >= midX and r >= midY : #4사
        return size*size*3 + funZ(midX, endX, midY, endY)
        

print(funZ(startX,endX,startY,endY))