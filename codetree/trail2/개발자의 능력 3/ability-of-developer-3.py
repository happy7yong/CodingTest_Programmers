abilities = list(map(int, input().split()))
total_sum = sum(abilities)

min_diff = 1000000

#각각의 값의 차이 최소화
def get_diff(i,j,k) :
    sum = abilities[i]+abilities[j]+abilities[k]
    return abs((total_sum - sum) - sum)


for i in range(len(abilities)) :
    for j in range(i+1,len(abilities)) :
        for k in range(j+1,len(abilities)) :
            min_diff = min(min_diff,get_diff(i,j,k))

print(min_diff)