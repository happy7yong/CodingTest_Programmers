n, m = map(int, input().split())

#n의 약수 == m의 약수 인데 가장 작은 약수임

def gcd(n,m) :
    n_divisor = []
    m_divisor = []
    #n의 약수 구하기 
    for i in range(1,n+1) :
        if n%i==0 :
            n_divisor.append(i)
    for i in range(1,m+1) :
        if m%i==0 :
            m_divisor.append(i)

    gcd_val = max(list(set(n_divisor) & set(m_divisor)))
    print(gcd_val)

gcd(n,m)