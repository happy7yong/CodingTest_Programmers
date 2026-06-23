str = input()

def isPalindrome(str) :
    if str == str[::-1] :
        return True
    else : return False

print("Yes" if isPalindrome(str) else "No")