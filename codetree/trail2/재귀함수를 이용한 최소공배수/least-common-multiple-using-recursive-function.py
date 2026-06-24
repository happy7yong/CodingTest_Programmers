import math

n = int(input())
arr = list(map(int, input().split()))

#최소공배수 :

def gcd(a,b) :
    return gcd(b,a%b) if b else a 

def lcm(a,b) :
    return a*b // gcd(a,b)

def f(idx) :
    if idx==0 : 
        return arr[0]
    return lcm(f(idx-1),arr[idx])

print(f(n-1))