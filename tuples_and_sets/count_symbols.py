word = input()
char_occurrences = {char: word.count(char) for char in word}

for char, count in sorted(char_occurrences.items()):
    print(f'{char}: {count} time/s')
