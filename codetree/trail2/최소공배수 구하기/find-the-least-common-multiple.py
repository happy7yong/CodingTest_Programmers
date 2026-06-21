n, m = map(int, input().split())

def lcm (n,m):
    min_val = min(n,m)
    max_val = max(n,m)
    cnt=0
    m_arr = []

    while True :
        cnt+=1
        m_arr.append(max_val*cnt)
        if min_val*cnt in m_arr :
            print(min_val*cnt)
            break

lcm(n,m)