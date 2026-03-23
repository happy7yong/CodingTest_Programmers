import sys

input = sys.stdin.readline

n = int(input())

def solution():
    if (n%4  == 0 and n%100 != 0) or n%400==0 : 
        return 1
    return 0


print(solution())