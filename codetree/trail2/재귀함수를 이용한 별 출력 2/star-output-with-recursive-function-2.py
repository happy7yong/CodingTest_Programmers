n = int(input())

def recursion(n) :
    if n==0:
        return 
    
    print(" ".join(n*"*"))
    recursion(n-1)
    print(" ".join(n*"*"))

recursion(n)