n_grades = int(input())
students = {}

for _ in range(n_grades):
    name, grade = input().split()

    if name not in students:
        students[name] = []

    students[name].append(float(grade))

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    grades = ' '.join(map(lambda x: f'{x:.2f}', grades))

    print(f'{name} -> {grades} (avg: {avg:.2f})')
