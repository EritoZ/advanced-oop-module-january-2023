from collections import deque


def math_operations(*args: float, **kwargs):

    float_nums = deque(args)
    letters_dict = kwargs

    while float_nums:

        for letter in letters_dict:

            if letter == 'a':
                letters_dict[letter] += float_nums.popleft()

            elif letter == 's':
                letters_dict[letter] -= float_nums.popleft()

            elif letter == 'd':
                num = float_nums.popleft()

                if num != 0:
                    letters_dict[letter] /= num

            elif letter == 'm':
                letters_dict[letter] *= float_nums.popleft()

            if not float_nums:
                break

    return '\n'.join(f'{key}: {value:.1f}' for key, value in sorted(letters_dict.items(), key=lambda x: (-x[1], x[0])))


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
