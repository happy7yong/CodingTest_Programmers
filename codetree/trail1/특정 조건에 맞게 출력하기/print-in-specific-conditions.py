inputList = list(map(int,input().split()))

for ele in inputList :
    if ele == 0:
        break;
    
    if ele%2==0 :
        print(ele//2,end=" ")
    else :
        print(ele+3,end=" ")