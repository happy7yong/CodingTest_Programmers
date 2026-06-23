text = input()
pattern = input()

print(text.index(pattern) if pattern in text else -1)