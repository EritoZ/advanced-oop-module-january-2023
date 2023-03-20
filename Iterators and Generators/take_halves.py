import sys

def solution():

    def integers():

        for num in range(1, sys.maxsize):
            yield num

    def halves():

        for num in integers():
            yield num * 0.5

    def take(n, seq):

        ints = [next(seq) for _ in range(n)]

        return ints

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))