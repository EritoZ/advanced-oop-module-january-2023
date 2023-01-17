n_lines = int(input())
intersections = []

for line in range(n_lines):
    range1, range2 = input().split('-')
    start1, end1 = range1.split(',')
    start2, end2 = range2.split(',')

    set1 = {n for n in range(int(start1), int(end1) + 1)}
    set2 = {n for n in range(int(start2), int(end2) + 1)}

    intersection = set1.intersection(set2)

    intersections.append(intersection)

longest_intersection = max(intersections, key=len)

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
