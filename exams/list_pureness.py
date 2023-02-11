from collections import deque


def best_list_pureness(numbers: list, k: int):
    numbers = deque(numbers)
    pureness_scores = []

    for rotation in range(k + 1):

        multiplied_numbers = [n * i for i, n in enumerate(numbers)]

        sum_multiplied_numbers = sum(multiplied_numbers)

        pureness_scores.append([sum_multiplied_numbers, rotation])

        numbers.rotate()

    max_pureness = max(pureness_scores, key=lambda x: x[0])

    return f'Best pureness {max_pureness[0]} after {max_pureness[1]} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)