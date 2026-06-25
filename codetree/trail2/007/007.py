secret_code, meeting_point, time = input().split()
time = int(time)

class Code :
    def __init__ (self,code,point,time) :
        self.c = code
        self.p = point
        self.t = time

code1 = Code(secret_code, meeting_point, time)
print("secret code :",code1.c)
print("meeting point :",code1.p)
print("time :",code1.t)
