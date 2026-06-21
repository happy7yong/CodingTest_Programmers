n = int(input())

def is_magic_number(n) :
    return n%2==0 and sum(map(int,list(str(n))))%5==0

print("Yes" if is_magic_number(n) else "No")

