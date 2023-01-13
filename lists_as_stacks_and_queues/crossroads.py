from collections import deque

green_light_sec = int(input())
pass_duration = int(input())
before_crossroad = deque()
passed = 0
crash = False

command = input()
while command != 'END':
    car_or_green = command

    if car_or_green != 'green':
        before_crossroad.append(car_or_green)
    else:

        time = green_light_sec + pass_duration

        while before_crossroad and time > pass_duration:
            car = before_crossroad.popleft()

            if len(car) > time:
                crash = True
                print(f'''A crash happened!
{car} was hit at {car[time]}.''')
                break

            passed += 1
            time -= len(car)

    if crash:
        break

    command = input()

if not crash:
    print(f'''Everyone is safe.
{passed} total cars passed the crossroads.''')
