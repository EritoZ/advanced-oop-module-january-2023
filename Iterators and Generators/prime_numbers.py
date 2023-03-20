def get_primes(n_list: list):

    for n in n_list:

        if n > 1:

            for i in range(2, n):

                if n % i == 0:
                    break

            else:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))