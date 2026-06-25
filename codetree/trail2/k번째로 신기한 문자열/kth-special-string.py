n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
cur_str = []

#문자열 t로 시작하는 단어인지 판단하는 함수
def isWordStart(t,word) :
    if t in word :
        return word.index(t) == 0
    else :
        return False

#문자열 t로 시작하는 단어
for word in str :
    if isWordStart(t,word) :
        cur_str.append(word)

cur_str.sort()
print(cur_str[k-1])