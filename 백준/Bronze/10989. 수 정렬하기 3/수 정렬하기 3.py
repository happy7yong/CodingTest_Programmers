import sys

input = sys.stdin.readline

n = int(input())
arr = [0]*10001

#인덱스를 값으로

for _ in range(n) :
    arr[int(input())] += 1

for _ in range(1,10001) : 
    if arr[_] :
        for i in range(arr[_]) :
            sys.stdout.write(str(_) + "\n")