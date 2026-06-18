import sys
inputList = list(map(int,input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize
for ele in inputList :
    if -999 == ele or 999 == ele :
        break;

    if max_val < ele:
        max_val = ele
    if min_val > ele :
        min_val = ele


print(max_val,min_val)