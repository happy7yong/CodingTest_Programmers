n = int(input())


def print_sum(n) :
    if n==1:
        return 1
    return n+print_sum(n-1)

print(print_sum(n))