n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

#n개의 원소 : arr
#m개의 순서쌍 : queries


for (a,b) in queries :
    sum=0
    for i in range(a-1,b) :
        sum+=arr[i]
    print(sum)