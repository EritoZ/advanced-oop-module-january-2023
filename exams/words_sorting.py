def words_sorting(*args):
    words = args
    words_values_dict = {}

    for word in words:
        words_values_dict[word] = sum(map(ord, tuple(word)))

    if sum(words_values_dict.values()) % 2 != 0:
        words_values_dict = sorted(words_values_dict.items(), key=lambda x: -x[1])
    else:
        words_values_dict = sorted(words_values_dict.items())

    return '\n'.join([f'{key} - {value}' for key, value in words_values_dict])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))