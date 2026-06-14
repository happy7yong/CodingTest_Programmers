inputList = list(map(int,input().split()))
arr = [ 0 for _ in range(7)]

for ele in inputList :
    arr[ele]+=1

for i in range(1,len(arr)) :
    print(f"{i} - {arr[i]}")