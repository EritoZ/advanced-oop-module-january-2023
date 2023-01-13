expression = input()
stack = []

for i, symbol in enumerate(expression):
    if symbol == '(':
        stack.append(i)

    elif symbol == ')':
        first_bracket = stack.pop()
        print(expression[first_bracket:i + 1])
