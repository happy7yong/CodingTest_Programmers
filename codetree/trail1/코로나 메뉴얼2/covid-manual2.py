n=3

arr = [0,0,0,0] # A B C D

for _ in range(3) :
    inputList = input().split()
    state, temp = inputList[0],int(inputList[1])
    
    if state == "Y" :
        if temp >= 37 :
            arr[0] +=1
        else :
            arr[2] +=1
    else :
        if temp >= 37 :
            arr[1] +=1
        else :
            arr[3] +=1


print(" ".join(map(str,arr)),end=" ")
if arr[0]>=2 :
    print("E")
