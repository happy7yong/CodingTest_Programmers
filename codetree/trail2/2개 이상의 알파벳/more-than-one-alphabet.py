str = input()

def count_alp(str) :
    a=str[0]
    if str.count(a) == len(str) :
        return False
    return True

print("Yes" if count_alp(str) else "No")