import sys
input = sys.stdin.readline

str = input()
ListStr = list(str)

for i in range(len(ListStr)):
    if ListStr[i].islower():
        ListStr[i] = ListStr[i].upper()
    elif ListStr[i].isupper():
        ListStr[i] = ListStr[i].lower()
        
print("".join(ListStr))
