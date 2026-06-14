arr= list(map(int,input().split()))
arr_sum = []
for ele in arr :
    if ele==0 :
        break;
    arr_sum.append(ele)

print(" ".join(map(str,arr_sum[::-1])))
