from collections import deque


def math_operations(*args: float, **kwargs):

    float_nums = deque(args)
    letters_dict = kwargs

    while float_nums:

        for letter in letters_dict:
            num = float_nums.popleft()

            if letter == 'a':
                letters_dict[letter] += num

            elif letter == 's':
                letters_dict[letter] -= num

            elif letter == 'd':
                if num != 0:
                    letters_dict[letter] /= num

            elif letter == 'm':
                letters_dict[letter] *= num

            if not float_nums:
                break

    return '\n'.join(f'{key}: {value:.1f}' for key, value in sorted(letters_dict.items(), key=lambda x: (-x[1], x[0])))
