import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split(" ")))
F = int(input())
count = 0;

for i in arr :
    if i == F : count+=1;
    

print(count)
    