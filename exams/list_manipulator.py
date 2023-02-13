from collections import deque


def list_manipulator(numbers_list: list, *args):
    numbers_list = deque(numbers_list)
    commands = args
    add_or_remove = commands[0]
    beginning_or_end = commands[1]
    numbers = commands[2:len(commands)]

    commands_dict = {
        ('add', 'beginning'): lambda nums: [numbers_list.appendleft(n) for n in numbers[::-1]],
        ('add', 'end'): lambda nums: [numbers_list.append(n) for n in numbers],
        ('remove', 'beginning'): lambda nums: [numbers_list.popleft() for _ in range(nums[0] if nums else 1)],
        ('remove', 'end'): lambda nums: [numbers_list.pop() for _ in range(nums[0] if nums else 1)],
    }

    commands_dict[(add_or_remove, beginning_or_end)](numbers)

    return list(numbers_list)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
