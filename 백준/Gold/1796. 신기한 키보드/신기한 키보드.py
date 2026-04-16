import sys
from collections import defaultdict

input = sys.stdin.readline


#1. 문자열 받아서 위치 배열 만들기

S = input().strip()

arr = defaultdict(list)

for i,v in enumerate(S) :
    arr[v].append(i)

indexArr = dict(arr)


letters = sorted(indexArr.keys())




#2. #dp[B][0] = (1)dp[A][0](전의 A를 처리한 비용) + (2)abs(전의 최종 거리(1일경우) - 현재 B의 거리()) + (3)B의 모든 요소를 이동했을 때의 거리 + (4)출력을 누른 횟수
#(2): dp[A] : 가장 오른쪽에서 끝났으니가, i_right 

dp = [ [0]*2 for i in range(len(letters))]

first = letters[0]

i_left = indexArr[first][0]
i_right = indexArr[first][len(indexArr[first])-1]

prev_left = indexArr[first][0]
prev_right = indexArr[first][len(indexArr[first])-1]

i_dict = abs(i_left - i_right)
printCount = len(indexArr[first])

dp[0][0] = abs(0-i_left) + i_dict + printCount
dp[0][1] = abs(0-i_right) + i_dict + printCount


for i in range(1,len(letters)) :
    ch = letters[i]
    
    #ch의 가장 왼쪽 위치 인덱스 : i_left
    i_left = indexArr[ch][0]
    #ch의 가장 오른쪽 위치 인덱스 : i_right
    i_right = indexArr[ch][len(indexArr[ch])-1]
    
    i_dict = abs(i_left - i_right)
    printCount = len(indexArr[ch])
    
    #dp[i][0] : 오른쪽 끝에서 끝남.-> 오른쪽에서 끝났으니까 prev_right에 최종 위치겠고, 이번 인덱스를 가장 왼쪽에서 오른쪽으로 이동시킬꺼라 i_left를 빼야됨. 
    dp[i][0] = min(dp[i-1][0] + abs(prev_right - i_left) + i_dict + printCount,
                   dp[i-1][1] + abs(prev_left - i_left) + i_dict + printCount)
    dp[i][1] = min(dp[i-1][0] + abs(prev_right - i_right) + i_dict + printCount,
                   dp[i-1][1] + abs(prev_left - i_right) + i_dict + printCount)
    
    prev_left = indexArr[ch][0]
    prev_right = indexArr[ch][len(indexArr[ch])-1]


print(min(*dp[-1]))