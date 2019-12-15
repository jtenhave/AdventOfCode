
# Read program data from a text file.
with open("i1.txt") as input:
    input = input.read().split(",")

program = {}

for i, v in enumerate(input):
    program[i] = int(v)

# Run the program with inputs.
def runProgram(i1, i2):
    programCopy = program.copy()
    programCopy[1] = i1
    programCopy[2] = i2

    pc = 0;
    code = programCopy[pc]

    while code != 99:
        
        p1 = programCopy[programCopy[pc + 1]]
        p2 = programCopy[programCopy[pc + 2]]
        o = programCopy[pc + 3]

        if (code == 1):
            programCopy[o] = p1 + p2;

        if (code == 2): 
            programCopy[o] = p1 * p2;
        
        pc += 4
        code = programCopy[pc]

    return programCopy[0]
