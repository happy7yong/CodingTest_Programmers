import sys
inputList = list(map(int,input().split()))

min_val_500up = 1000
max_val_500down = 0

for ele in inputList :
    if ele >= 500 :
        if min_val_500up > ele :
            min_val_500up = ele
    else :
        if max_val_500down < ele :
            max_val_500down = ele

print(max_val_500down,min_val_500up)
