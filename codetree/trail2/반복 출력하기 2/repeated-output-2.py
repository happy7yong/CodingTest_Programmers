n = int(input())

def str_print(n) :
    if n==0 :
        return 
    str_print(n-1)
    print("HelloWorld")

str_print(n)