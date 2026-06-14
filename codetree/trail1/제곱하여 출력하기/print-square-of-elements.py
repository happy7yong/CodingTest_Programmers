n = int(input()) 
arr = list(map(int,input().split()))
answer = [ ele**2 for ele in arr]
print(" ".join(map(str,answer)))
