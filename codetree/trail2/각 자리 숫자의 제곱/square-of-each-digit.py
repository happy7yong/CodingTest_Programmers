n = int(input())

def print_sq(n) :
    if n < 10 :
        return n**2
    
    return print_sq(n//10) + (n%10)**2

print(print_sq(n))