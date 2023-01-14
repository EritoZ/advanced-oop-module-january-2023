nums = tuple(map(float, input().split()))
formatted_nums = []

[formatted_nums.append(f'{number} - {nums.count(number)} times') for number in nums
 if f'{number} - {nums.count(number)} times' not in formatted_nums]

print('\n'.join(formatted_nums))
