def solution(n):
    answer = 1
    pizza_count = 0
    
    #pizza 갯수 증가 시키기 
    while answer!=0:
        pizza_count+=1
        answer = (6*pizza_count)%n
    return pizza_count