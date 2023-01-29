def students_credits(*args):
    diyan_dict = {}
    message = []

    for course in args:
        course_name, credits, max_test_points, diyans_points = course.split('-')

        acquired_credits = int(credits) * (int(diyans_points) / int(max_test_points))

        diyan_dict[course_name] = acquired_credits

    total_diyan_credits = sum(diyan_dict.values())

    if total_diyan_credits >= 240:
        message.append(f"Diyan gets a diploma with {total_diyan_credits:.1f} credits.")
    else:
        message.append(f"Diyan needs {240 - total_diyan_credits:.1f} credits more for a diploma.")

    [message.append(f'{course[0]} - {course[1]:.1f}') for course in sorted(diyan_dict.items(), key=lambda x: -x[1])]

    return '\n'.join(message)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)