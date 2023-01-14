def sum_pairs(nums_iterable, target_sum):
    for n in range(1, len(nums_iterable)):
        if nums_iterable[0] + nums_iterable[n] == target_sum:
            print(f'{nums_iterable.pop(0)} + {nums_iterable.pop(n - 1)} = {target_num}')
            break
    else:
        return

    sum_pairs(nums_iterable, target_sum)


nums = list(map(int, input().split()))
target_num = int(input())

sum_pairs(nums, target_num)
