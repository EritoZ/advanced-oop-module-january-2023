def numbers_searching(*args):
    numbers = args
    smallest_n = min(numbers)
    biggest_n = max(numbers)

    duplicates = sorted([n for n in set(numbers) if numbers.count(n) > 1 and smallest_n <= n <= biggest_n])

    missing_n = [n for n in range(smallest_n, biggest_n) if n not in numbers]

    return [missing_n[-1], duplicates]

