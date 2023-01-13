stack = []

n_ques = int(input())

for _ in range(n_ques):
    command = input().split()

    if command[0] == '1':
        n = int(command[1])

        stack.append(n)

    elif command[0] == '2':
        if stack:
            stack.pop()

    elif command[0] == '3':
        if stack:
            print(max(stack))

    elif command[0] == '4':
        if stack:
            print(min(stack))

print(', '.join([str(n) for n in stack][::-1]))
