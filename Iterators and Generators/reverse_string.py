def reverse_text(string):

    for l in reversed(string):
        yield l


for char in reverse_text("step"):
    print(char, end='')