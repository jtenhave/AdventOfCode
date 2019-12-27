from common.computer import Computer
import itertools

# Read program data from a text file.
with open("Day7/i1.txt") as input:
    program = input.read()

# Initialize the amps.
amps = []
for _ in range(0, 5):
    amp = Computer()
    amp.loadProgram(program); 
    amps.append(amp)

maxOutput = 0
sequences = list(itertools.permutations([5, 6, 7, 8, 9]))

for sequence in sequences:

    for i in range(0, 5):
        amp = amps[i]
        amp.resetProgram()
        amp.pushInput([sequence[i]])

    lastOutput = 0
    while not amps[4].finished:
        for i in range(0, 5):
            amp = amps[i]
            amp.pushInput([lastOutput])
            amp.runProgram()

            lastOutput = amp.outputBuffer[-1]

    if amps[4].outputBuffer[-1] > maxOutput:
        maxOutput = lastOutput

print(maxOutput)

