from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()

        result = func(*args, **kwargs)

        end = time()

        print(f'Function speed {end - start}')

        return result

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())