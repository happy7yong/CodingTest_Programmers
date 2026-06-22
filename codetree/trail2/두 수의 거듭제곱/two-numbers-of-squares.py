a, b = map(int, input().split())

def dubleDeci(a,b) :
    sum = 1
    for _ in range(b) :
        sum*=a
    return sum

print(dubleDeci(a,b))