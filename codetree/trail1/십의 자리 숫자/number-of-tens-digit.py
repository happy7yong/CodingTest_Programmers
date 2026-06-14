inputList = list(map(int,input().split()))
arr = []
arr = [ 0 for _ in range(10)]

for ele in inputList :
    if ele == 0:
        break;
    arr.append(ele//10)

for ele in arr :
    arr[ele]+=1

for i in range(1,10) :
    print(f"{i} - {arr[i]}")

