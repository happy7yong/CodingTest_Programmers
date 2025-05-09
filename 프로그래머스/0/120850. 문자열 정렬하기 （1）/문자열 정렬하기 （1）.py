def solution(my_string):
    answer = [int(x) for x in list(my_string) if x.isdigit()]
    
    return sorted(answer)