n_el_first_set, n_el_second_set = input().split()
first_set = {input() for n in range(int(n_el_first_set))}
second_set = {input() for num in range(int(n_el_second_set))}

diff = first_set.intersection(second_set)

print('\n'.join(diff))
