
import sys
n = int(input())
price = list(map(int, input().split()))

#price는 주식장 변화하는 가격
#일단 가장 낮은 가격에 사서 오른쪽 배열 잘라서 가장 높은 가격대 선택
#3 13 2 5 
#이때는 3 13이 더 이득이니까 
# for문으로 돌려가면서 min계산과 gap 차이를 계산해야할것같음

min_val = sys.maxsize
max_gap = -sys.maxsize

for ele in price :
    if min_val > ele :
        min_val = ele
    gap = ele - min_val
    if max_gap < gap:
        max_gap = gap

print(max_gap)
    

