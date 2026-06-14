n = int(input())
inputList = list(map(int,input().split()))
answerList = []

for ele in inputList :
    if ele%2==0:
        answerList.append(ele)

print(" ".join(map(str,answerList[::-1])))
