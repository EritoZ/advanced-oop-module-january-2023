def addition(sub_ex):
    while len(sub_ex) > 1:
        sub_ex[0] += sub_ex.pop(1)

    return sub_ex


def subtraction(sub_ex):
    while len(sub_ex) > 1:
        sub_ex[0] -= sub_ex.pop(1)

    return sub_ex


def division(sub_ex):
    while len(sub_ex) > 1:
        sub_ex[0] //= sub_ex.pop(1)

    return sub_ex


def multiplication(sub_ex):
    while len(sub_ex) > 1:
        sub_ex[0] *= sub_ex.pop(1)

    return sub_ex


operator_dict = {
    '+': lambda x: addition(x),
    '-': lambda x: subtraction(x),
    '/': lambda x: division(x),
    '*': lambda x: multiplication(x)
}
expression = input().split()

while len(expression) > 1:

    sub_expression = []
    for i, symbol in enumerate(expression):

        if symbol in operator_dict:
            sub_expression = operator_dict[symbol](sub_expression)

            expression[:i + 1] = sub_expression
            break

        else:
            sub_expression.append(int(symbol))

print(expression[0])
