inputList = list(map(int,input().split()))
arr = []
score = [ 0 for _ in range(11)]

for ele in inputList :
    if ele ==0:
        break;
    arr.append(ele//10)

for ele in arr :
    score[ele]+=1

for i in range(len(score)-1,0,-1) :
    print(f"{i*10} - {score[i]}")

