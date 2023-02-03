from collections import deque

vowels = deque(input().split())
consonants = input().split()
flowers = {
    "rose": 'rose',
    "tulip": 'tulip',
    "lotus": "lotus",
    "daffodil": "daffodil"
}
found_flower = ''

while vowels and consonants and not found_flower:

    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers:

        flowers[flower] = flowers[flower].replace(consonant, '')

        flowers[flower] = flowers[flower].replace(vowel, '')

        if not flowers[flower]:
            found_flower = flower
            break

if found_flower:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
