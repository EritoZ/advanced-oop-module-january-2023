from collections import deque

males = [int(male) for male in input().split() if int(male) > 0]
females = deque([int(female) for female in input().split() if int(female) > 0])
matches = 0

while males and females:

    if males[-1] % 25 == 0:
        for _ in range(2):
            males.pop()

            if not males:
                break

        continue

    elif females[0] % 25 == 0:
        for _ in range(2):
            females.popleft()

            if not females:
                break

        continue

    current_male = males.pop()
    current_female = females.popleft()

    if current_female != current_male:
        current_male = current_male - 2

        if current_male > 0:
            males.append(current_male)

    else:
        matches += 1

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
