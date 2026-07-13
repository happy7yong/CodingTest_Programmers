n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
# a, b, c = zip(*moves)
# a, b, c = list(a), list(b), list(c)



#최대 점수 얻기
max_val = 0

#종이 컵 선택
for i in range(1,4) :
    score = 0
    #시뮬레이션 시작
    arr = [0,0,0,0] #0 1 2
    arr[i] = 1
    for a,b,c in moves :
        arr[a],arr[b] = arr[b],arr[a]
        if arr[c] == 1 :
            score+=1
    max_val = max(max_val,score)

print(max_val)

        
