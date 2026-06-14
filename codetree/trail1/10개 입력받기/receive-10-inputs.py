inp = list(map(int,input().split()))
arr = []

for ele in inp :
    if ele ==0 :
        break;
    arr.append(ele)
print(sum(arr),round(sum(arr)/len(arr),1))