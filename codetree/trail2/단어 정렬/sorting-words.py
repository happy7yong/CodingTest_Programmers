n = int(input())
word = [input() for _ in range(n)]

word.sort()

print("\n".join(word))