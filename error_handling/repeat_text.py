text = input()

try:
    integer = int(input())

    print(text * integer)

except ValueError:
    print("Variable times must be an integer")


