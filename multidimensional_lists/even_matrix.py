rows = int(input())
even_els = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for row in range(rows)]

print(even_els)
