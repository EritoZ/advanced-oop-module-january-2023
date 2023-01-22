nums = input().split('|')

for values in nums[::-1]:
    values = values.split()

    if values:
        print(' '.join(values), end=' ')
