import sys

n = int(input())
arr = list(map(int, input().split()))

min = sys.maxsize

for ele in arr :
    if min > ele :
        min = ele

print(min,end=" ")

print(arr.count(min))