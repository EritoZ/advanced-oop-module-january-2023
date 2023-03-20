def read_next(*args):

    for seq in args:
        for el in seq:
            yield el


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
