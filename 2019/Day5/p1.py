from common.computer import Computer

# Read program data from a text file.
with open("Day5/i1.txt") as input:
    program = input.read()

# Initialize the program.
computer = Computer()
computer.loadProgram(program);
computer.pushInput([1])

# Run the program.
computer.runProgram()

# Print the output.
computer.printOutput()
