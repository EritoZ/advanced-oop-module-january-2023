from itertools import permutations


def possible_permutations(nums: list):

    for i in permutations(nums):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]