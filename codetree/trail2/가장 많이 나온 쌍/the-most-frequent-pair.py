n, m = map(int, input().split())
pairs = [tuple(sorted(map(int, input().split()))) for _ in range(m)]

pairs_only = []
num = []



for ele in pairs :
    if ele in pairs_only: 
        idx = pairs_only.index(ele)
        num[idx]+=1
    else :
        pairs_only.append(ele)
        num.append(1)
    

print(max(num))