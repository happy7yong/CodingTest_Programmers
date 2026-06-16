n=int(input())
cnt=0
idx_answer = 0

inputList = list(map(int,input().split()))

for idx,ele in enumerate(inputList) :
    if ele == 2 :
        cnt+=1
    if cnt == 3 :
        idx_answer = idx+1
        break


print(idx_answer)