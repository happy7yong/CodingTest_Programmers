inputList = list(map(int,input().split()))
arr = []
cnt=0 ; sum=0

#입력완료
for ele in inputList :
    if ele==0:
        break;
    arr.append(ele)

for ele in arr :
    if ele%2==0:
        sum+=ele
        cnt+=1

print(cnt, sum)