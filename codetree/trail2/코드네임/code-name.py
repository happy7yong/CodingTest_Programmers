MAX_N = 5

class User :
    def __init__(self,score=0,codename="") :
        self.cn = codename
        self.s = score

users = []

for _ in range(MAX_N):
    codename, score = input().split()
    score = int(score)
    users.append(User(score,codename))
    

#5명의 코드네임, 점수 입력 -> 점수가 제일 낮은 요원의 정보를 출력함.
Min_val = 100
user_answer = ""
for user in users :
    if Min_val > user.s :
        Min_val = user.s
        user_answer = user
print(user_answer.cn,user_answer.s)
