inputList = list(map(int,input().split()))

n=10
print(sum(inputList[1::2]),end=" ")
fillter_3 = inputList[2::3]
print(round(sum(fillter_3)/len(fillter_3),1))