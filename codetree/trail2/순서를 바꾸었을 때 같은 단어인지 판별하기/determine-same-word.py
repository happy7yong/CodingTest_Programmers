word1 = input()
word2 = input()

w1 = sorted(list(word1))
w2 = sorted(list(word2))

print("Yes" if w1 == w2 else "No")