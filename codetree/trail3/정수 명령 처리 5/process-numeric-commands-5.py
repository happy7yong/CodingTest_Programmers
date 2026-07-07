N = int(input())

arr = []
line = []

for _ in range(N):
    commands = input().split()
    command = commands[0]

    if command == "push_back":
        number = int(commands[1])
        arr.append(number)
    elif command == "pop_back" :
        arr.pop()
    elif command == "size" :
        line.append(len(arr))
    elif command == "get" :
        number = int(commands[1])
        line.append(arr[number-1])

print("\n".join(map(str,line)))




