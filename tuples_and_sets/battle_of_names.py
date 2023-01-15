n_names = int(input())
odd = set()
even = set()

for row in range(1, n_names + 1):
    value = sum(map(ord, input())) // row

    if value % 2 != 0:
        odd.add(value)

    else:
        even.add(value)

sum_odd = sum(odd)
sum_even = sum(even)

if sum_odd == sum_even:
    print(', '.join(map(str, odd.union(even))))

elif sum_odd > sum_even:
    print(', '.join(map(str, odd.difference(even))))

else:
    print(', '.join(map(str, odd.symmetric_difference(even))))
