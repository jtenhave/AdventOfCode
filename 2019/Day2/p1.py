from common.computer import Computer

# Read program data from a text file.
with open("Day2/i1.txt") as input:
    program = input.read()

# Initialize the program.
computer = Computer()
computer.loadProgram(program);

# Set the initial state.
computer.program[1] = 12;
computer.program[2] = 2;

# Run the program.
computer.runProgram()

print(computer.program[0])
