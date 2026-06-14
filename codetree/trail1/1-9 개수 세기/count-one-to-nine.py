n=int(input())
inputList = list(map(int,input().split()))
arr = [ 0 for i in range(10)]


for ele in inputList :
    arr[ele]+=1

print("\n".join(map(str,arr[1::])))
    