import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque();



for i in range(1,n+1) :
    arr.append(i)

while(len(arr) > 1):
    arr.popleft();
    n = arr.popleft();
    arr.append(n)
    
print(arr.pop())