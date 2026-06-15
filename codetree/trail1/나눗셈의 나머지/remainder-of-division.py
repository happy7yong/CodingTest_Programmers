a,b = map(int,input().split())


relist = [ 0 for _ in range(b)]#b

re = 0;

while a>1 : 
    re = a%b
    a = a//b #반복
    relist[re] +=1

answer = [ ele**2 for ele in relist]

print(sum(answer))

