binary = input()

sum=0
idx = 0
list_b = list(binary)
binary_arr = list(map(int,list_b))
for i in range(len(binary)-1,-1,-1) :
    sum+=binary_arr[idx]*2**i
    idx+=1

print(sum)

