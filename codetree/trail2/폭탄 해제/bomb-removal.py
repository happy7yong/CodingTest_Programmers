class TNT :
    def __init__(self,unlock_code, wire_color, seconds):
        self.code = unlock_code
        self.color = wire_color
        self.seconds = seconds

unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

tnt1 = TNT(unlock_code, wire_color, seconds)

print("code :",tnt1.code)
print("color :",tnt1.color)
print("second :",tnt1.seconds)

