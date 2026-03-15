import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split(" ")))

m = int(input());
arrM = list(map(int,input().split(" ")))

arr.sort();

answer = [];

def solution(searchNum) :
    leftIndex = 0;
    rightIndex = n-1;
    
    while(leftIndex <= rightIndex):
        midIndex = (leftIndex+rightIndex)//2
        
        if arr[midIndex] == searchNum : return 1;
        
        if arr[midIndex] < searchNum :
            leftIndex = midIndex + 1;
        elif arr[midIndex] > searchNum :
            rightIndex = midIndex - 1;
    
    return 0;
    

for i in range(m) : 
    answer.append(solution(arrM[i]))
    
    


print(*answer)