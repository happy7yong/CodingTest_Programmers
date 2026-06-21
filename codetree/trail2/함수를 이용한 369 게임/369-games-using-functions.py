a, b = map(int, input().split())
cnt =0

def d_369(ele) :
    return ele == 3 or ele ==6 or ele == 9


def is_magic_number(n) :
    arr = map(int,list(str(n)))

    for ele in arr :
        if d_369(ele) :
            return True
    
    if n%3==0 :
        return True

    return False

for i in range(a,b+1) :
    if is_magic_number(i) :
        cnt+=1

print(cnt)