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
sequences = list(itertools.permutations([0, 1, 2, 3, 4]))

for sequence in sequences:
    
    lastOutput = 0
    for i in range(0, 5):
        amp = amps[i]
        amp.resetProgram()
        amp.pushInput([sequence[i], lastOutput])
        amp.runProgram()

        lastOutput = amp.outputBuffer[0]

    if lastOutput > maxOutput:
        maxOutput = lastOutput

print(maxOutput)

