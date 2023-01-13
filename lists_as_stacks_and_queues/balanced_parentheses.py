bracket_list = ['(', ')', '{', '}', '[', ']']
bracket_indexes = []
brackets = input()

for bracket in brackets:

    if bracket_indexes and bracket_indexes[-1] + 1 == bracket_list.index(bracket):
        bracket_indexes.pop()
    else:
        bracket_indexes.append(bracket_list.index(bracket))

if not bracket_indexes:
    print('YES')
else:
    print('NO')
    