from common.computer import Computer

# Read program data from a text file.
with open("Day2/i1.txt") as input:
    program = input.read()

# Initialize the program.
computer = Computer()
computer.loadProgram(program);

# Run the program until the correct inputs are found.
for i in range(99):
    for j in range (99):

        # Set the initial state.
        computer.program[1] = i;
        computer.program[2] = j;

        computer.runProgram()

        # Test if the desired output was found.
        if (computer.program[0] == 19690720):
            print(100 * i + j)
            exit()
        
        computer.resetProgram()
        