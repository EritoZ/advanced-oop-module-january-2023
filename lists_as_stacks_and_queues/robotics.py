from collections import deque


def change_time(timer):
    if timer[-1] >= 60:
        timer[1] += timer[-1] // 60
        timer[-1] %= 60

        if timer[1] >= 60:
            timer[0] += timer[1] // 60
            timer[1] %= 60

            if timer[0] >= 24:
                timer[0] %= 24

    return timer


def get_products():
    products = deque([])

    command = input()
    while command != 'End':
        products.append(command)

        command = input()

    return products


robots = input().split(';')
robots = deque([[robot, index] for index, robot in enumerate(robots)])
robot_indexes = []
time = list(map(int, input().split(':')))
working_robots = {}
all_products = get_products()

while all_products:
    time[-1] += 1
    time = change_time(time)

    if str(time) in working_robots:
        [robots.insert(robot[1], robot) for robot in working_robots[str(time)]]
        working_robots.pop(str(time))

    if robots:
        product = all_products.popleft()

        robot = robots.popleft()
        robot_info = robot[0].split('-')
        robot_name = robot_info[0]
        robot_proc_time = int(robot_info[-1])

        robot_timer = str(change_time([time[0], time[1], time[-1] + robot_proc_time]))

        if robot_timer not in working_robots:
            working_robots[robot_timer] = []

        working_robots[robot_timer].append(robot)

        print(f'{robot_name} - {product} [{time[0]:02d}:{time[1]:02d}:{time[-1]:02d}]')
    else:
        all_products.append(all_products.popleft())
