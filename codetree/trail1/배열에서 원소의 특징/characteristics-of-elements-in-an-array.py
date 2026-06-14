inputList = list(map(int,input().split()))
first = 0

for ele in inputList : 
    if ele%3==0 :
        print(first)
        break
    first = ele
