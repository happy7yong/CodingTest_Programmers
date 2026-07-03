n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

x,y = zip(*commands)
total = sum(map(int,x))

arr = [""] * (2*(total+1))
cur = total+1

#일직선으로 된 회색타일
#L  흰색
#R 검은색
#검은색 타일 수 출력하기

#알아야하는 값
#1. 마지막으로 뒤집은 타일 -> 추적할 필요 없음
#2. 검은색 타일 수 
#왼쪽이나 오른쪽으로 이동하기

#이동하기 
for num, direction in commands:
    num=int(num)
    if direction == "R" : #오른쪽으로 증가
        for i in range(cur,cur+num):
            arr[i] = "B"
        cur=cur+num-1
    elif direction == "L" : #왼쪽으로 증가
        for i in range(cur,cur-num,-1) :
            arr[i] = "W"
        cur=cur-num+1

#횟수 세기
w = arr.count("W")
b = arr.count("B")
print(w,b)

