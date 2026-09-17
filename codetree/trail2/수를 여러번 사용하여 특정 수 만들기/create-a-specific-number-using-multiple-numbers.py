a,b,c = map(int, input().split())

max_val = 0

for a_x in range(0,(c//a)+1) :

    for b_x in range(0, (c//b)+1) :
        cur_val = (a*a_x) + b*b_x 
        if cur_val <= c:
            max_val = max(max_val, cur_val)

print(max_val)