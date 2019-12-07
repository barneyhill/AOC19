def read_input():
    with open("input.txt") as f:
        file = f.read()
    file = file.split(',')
    file = [int(x) for x in file]
    return file

file = read_input()

#part one
file[1] = 12
file[2] = 2

def run(opcode):
    pointer = 0
    while opcode[pointer] != 99:
        if opcode[pointer] == 1:
            opcode[opcode[pointer+3]] = opcode[opcode[pointer+1]] + opcode[opcode[pointer+2]]
        if opcode[pointer] == 2:
            opcode[opcode[pointer + 3]] = opcode[opcode[pointer + 1]] * opcode[opcode[pointer + 2]]
        pointer += 4
    return opcode[0]

file[1] = 12
file[2] = 2
print(run(file))

def find_nv():
    for noun in range(0, 100):
        for verb in range(0,100):
            file = read_input()
            file[1] = noun
            file[2] = verb
            if run(file) == 19690720:
                return noun,verb
print(find_nv())
