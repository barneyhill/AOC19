def read_input():
    with open("input.txt") as f:
        file = f.readlines()
    file = [x.strip() for x in file]
    file = [int(x) for x in file]
    return file

file = read_input()

#part one

def fuel(mass):
    return int(mass/3)-2
total = 0
for mass in file:
    total += fuel(mass)

print(total)

#part two

total = 0
for mass in file:
    total -= mass
    while mass > 0:
        total += mass
        print(mass)
        mass = fuel(mass)
    print('\n')
print(total)