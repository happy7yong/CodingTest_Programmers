pp,p = map(int,input().split())
#a = 첫번째 b= 두번째
answer = [pp,p];
n=10
for _ in range(n) :
    pp, p = p,pp+p
    answer.append(p%10)

print(" ".join(map(str,answer[:10])))
