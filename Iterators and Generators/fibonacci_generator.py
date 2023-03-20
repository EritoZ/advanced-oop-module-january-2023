import sys


def fibonacci():
    fibonacci_seq = [0, 1]

    yield fibonacci_seq[0]

    for n in range(1, sys.maxsize):
        yield fibonacci_seq[n]

        fibonacci_seq.append(fibonacci_seq[n] + fibonacci_seq[n - 1])


generator = fibonacci()
for i in range(5):
    print(next(generator))