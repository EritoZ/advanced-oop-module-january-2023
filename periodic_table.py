n_input = int(input())
periodic_table = {el for line in range(n_input) for el in input().split()}

print('\n'.join(periodic_table))
