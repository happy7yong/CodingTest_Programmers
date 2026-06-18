n = int(input())
a = list(map(int, input().split()))

#배열에서 최댓값 max로 찾고 > index로 찾고 >  slice로 반 잘라서 왼쪽까지만 잘라서 
#다시 배열에서 최댓값 max로 찾고 >index로 찾고
#그 배열의 최솟값이 있을때까지 자름.

max_val = 0;

while True :
    max_val=max(a)
    index_val = a.index(max_val)
    print(index_val+1,end=" ")
    a = a[:index_val:]
    if len(a) < 1 :
        break
