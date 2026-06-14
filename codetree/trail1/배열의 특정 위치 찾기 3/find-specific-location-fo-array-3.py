inputList = list(map(int,input().split()))
arr = []

for ele in inputList :
    if ele==0 :
        break
    arr.append(ele)

print(arr[-1]+arr[-2]+arr[-3])