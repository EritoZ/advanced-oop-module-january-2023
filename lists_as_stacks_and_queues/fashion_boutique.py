clothes = list(map(int, input().split()))
capacity_rack = int(input())
rack = capacity_rack
used_rack = 1

while clothes:

    if rack - clothes[-1] < 0:
        rack = capacity_rack
        used_rack += 1

    rack -= clothes.pop()

print(used_rack)
