import requests

def day_3_get_and_process_data(url, cookies):
    raw_data = requests.get(url, cookies=cookies).text.strip()
    return raw_data.split('\n')

def get_points(start, start_steps, move):
    delta = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    
    direction, distance = move[0], int(move[1:])
    x, y = start
    dx, dy = delta[direction]
    result = {}

    for _ in range(distance):
        x += dx
        y += dy
        start_steps += 1
        result[(x, y)] = start_steps
    
    return result, (x, y), start_steps
    
def get_all_points(moves):
    result = {}
    start = (0,0)
    total_steps = 0

    for move in moves.split(','):
        points, start, total_steps = get_points(start, total_steps, move)
        result.update(points)
        return result

def day_3_problems(url, cookies):
    first_moves, second_moves = day_3_get_and_process_data(url, cookies)

    first_points = get_all_points(first_moves)
    second_points = get_all_points(second_moves)

    intersections = first_points.keys() & second_points.keys()

    solution_1 = min(abs(a) + abs(b) for a, b in intersections)
    solution_2 = min(first_points[point] + second_points[point] for point in intersections)

    print(f'solution 1: {solution_1}')
    print(f'solution 2: {solution_2}')


day_3_problems('https://adventofcode.com/2019/day/3/input', '53616c7465645f5fb32084537a65e80b3ec46d1b9c93e489eded1fc1166b26ba35c1c9380057d4cb7801cb2d154c7a69')