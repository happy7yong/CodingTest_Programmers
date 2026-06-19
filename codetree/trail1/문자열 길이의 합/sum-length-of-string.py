n = int(input())

arr = [ input() for i in range(n)]

sum = 0
a_count = 0

for ele in arr :
    sum+=len(ele)
    if ele[0] == "a" :
        a_count+=1

print(sum, a_count)