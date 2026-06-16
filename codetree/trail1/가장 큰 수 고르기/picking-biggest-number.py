import sys

inputList = list(map(int,input().split()))

max_val = -sys.maxsize

for ele in inputList :
    if max_val <= ele :
        max_val = ele

print(max_val)