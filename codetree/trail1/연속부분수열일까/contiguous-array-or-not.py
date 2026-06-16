an,bn=map(int,input().split())
a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))


a_str_arr="".join(map(str,a_arr))
b_str_arr="".join(map(str,b_arr))

if b_str_arr in a_str_arr :
    print("Yes")
else :
    print("No")
    



