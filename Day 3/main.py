import math

def read_input():
    with open("input.txt") as f:
        file = f.readlines()
    file[0] = file[0].split(',')
    file[1] = file[1].split(',')
    return file

file = read_input()

def get_points(directions):
    current = [0,0]
    travel = 0
    points = set()
    for direction in directions:
        if direction[0] == 'R':
            for change in range(1,int(direction[1:])+1):
                travel += 1
                current[0] += 1
                points.add(str(current[:]+[travel]))
        if direction[0] == 'L':
            for change in range(1,int(direction[1:])+1):
                travel += 1
                current[0] -= 1
                points.add(str(current[:]+[travel]))
        if direction[0] == 'D':
            for change in range(1,int(direction[1:])+1):
                travel += 1
                current[1] -= 1
                points.add(str(current[:]+[travel]))
        if direction[0] == 'U':
            for change in range(1,int(direction[1:])+1):
                travel += 1
                current[1] += 1
                points.add(str((current[:]+[travel])))
    return points

exclude =  get_points(file[0])
[print(x) for x in get_points(file[1])]
new_list = [x for x in get_points(file[1]) if x in exclude]

smallest = math.inf

for coord in new_list:
    coord = coord[1:-1].split(',')
    dist = math.sqrt(int(coord[0])**2+int(coord[1])**2)
    if dist < smallest:
        smallest = dist

print(smallest)