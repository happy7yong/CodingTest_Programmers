n=int(input())
plug = False

for i in range(2,n) :
    if n%i==0 :
        plug=True
        break;

if plug :
    print("C")
else :
    print("N")