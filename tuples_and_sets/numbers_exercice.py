first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n_lines = int(input())

for line in range(n_lines):
    command = input()

    if command == 'Check Subset':
        if first_sequence.issubset(second_sequence) or first_sequence.issuperset(second_sequence):
            print(True)
        else:
            print(False)
    else:
        command = command.split()
        current_command = ' '.join(command[:2])
        nums = set(map(int, command[2:]))

        if current_command == 'Add First':
            first_sequence.update(nums)

        elif current_command == 'Add Second':
            second_sequence.update(nums)

        elif current_command == 'Remove First':
            first_sequence.difference_update(nums)

        elif current_command == 'Remove Second':
            second_sequence.difference_update(nums)

print(', '.join(map(str, sorted(first_sequence))))
print(', '.join(map(str, sorted(second_sequence))))
