from collections import deque

seats = input().split(', ')
nums1 = deque(input().split(', '))
nums2 = deque(input().split(', '))
taken_seats = []
taken_seats_n = 0
rotations = 0

while taken_seats_n != 3 and rotations != 10:

    first_n = nums1.popleft()
    second_n = nums2.pop()

    ascii_chr = chr(int(first_n) + int(second_n))

    seat_v1 = first_n + ascii_chr
    seat_v2 = second_n + ascii_chr

    if seat_v1 in seats:

        if seat_v1 not in taken_seats:
            taken_seats.append(seat_v1)
            taken_seats_n += 1

    elif seat_v2 in seats:

        if seat_v2 not in taken_seats:
            taken_seats.append(seat_v2)
            taken_seats_n += 1

    else:
        nums1.append(first_n)
        nums2.appendleft(second_n)

    rotations += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
