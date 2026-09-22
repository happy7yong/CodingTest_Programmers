n = int(input())
seat = list(map(int,list(input())))

max_dist = 0

def distFind(cur_seat):
    curIdx = n
    preIdx = curIdx
    min_dist = n

    for curIdx in range(n) :
        if cur_seat[curIdx] == 1 :
            # print(preIdx,curIdx)
            cur_dist = abs(preIdx - curIdx)
            min_dist = min(min_dist,cur_dist)
            preIdx = curIdx
    return min_dist

#초기화
cur_seat=seat[:]
for fIdx in range(0,len(cur_seat)) :
    if cur_seat[fIdx] == 0 :
        cur_seat[fIdx] = 1
        #두번째 사람 찾기
        for sIdx in range(fIdx+1,len(cur_seat)) :
            #두번째도 찾음
            if cur_seat[sIdx] == 0 :
                cur_seat[sIdx] = 1
                # print(cur_seat)
        
                max_dist = max(max_dist, distFind(cur_seat))
                #두번째 되돌리기
                cur_seat[sIdx] = 0
        cur_seat[fIdx] = 0
        

print(max_dist)