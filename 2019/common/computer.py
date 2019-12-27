import re

opCodePattern = re.compile("(\d*?)(\d{1,2})$")

# A class that represents an instruction for the Intcode computer. 
class Instruction: 
    def __init__(self):
        self.parameters = 0
        self.result = True
        self.output = False
        self.jumps = False

    # Returns the size of the instruction.
    def size(self):
        return 1 + self.parameters + (1 if self.result else 0)

# A class that represents an Add instruction for the Intcode computer.
class Add(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2

    # Executes the instruction.
    def execute(self, params):
        return params[0] + params[1]

# A class that represents a Multiply instruction for the Intcode computer.
class Multiply(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2

    # Executes the instruction.
    def execute(self, params):
        return params[0] * params[1]

# A class that represents an Input instruction for the Intcode computer.
class Input(Instruction):
    def __init__(self, input):
        super().__init__()
        self.input = input
    
    # Executes the instruction.
    def execute(self, params):
        return self.input

# A class that represents an Output instruction for the Intcode computer.
class Output(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 1
        self.result = False
        self.output = True

    # Executes the instruction.
    def execute(self, params):
        return params[0]

# A class that represents a Jump-If-True instruction for the Intcode computer.
class JumpIfTrue(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.result = False
        self.jumps = True

    # Executes the instruction.
    def execute(self, params):
        return params[1] if params[0] != 0 else None

# A class that represents a Jump-If-False instruction for the Intcode computer.
class JumpIfFalse(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.result = False
        self.jumps = True

    # Executes the instruction.
    def execute(self, params):
        return params[1] if params[0] == 0 else None

# A class that represents a Less-Than instruction for the Intcode computer.
class LessThan(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2

    # Executes the instruction.
    def execute(self, params):
        return 1 if params[0] < params[1] else 0

# A class that represents an Equals instruction for the Intcode computer.
class Equals(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2

    # Executes the instruction.
    def execute(self, params):
        return 1 if params[0] == params[1] else 0

# A class that represents an Intcode computer. Used by Day 2, 5, 7.
class Computer:

    # Load a program into the computer.
    def loadProgram(self, program):

        self.programBase = {}

        for i, v in enumerate(program.split(",")):
            self.programBase[i] = int(v)

        self.resetProgram()

    # Resets the program to the loaded state.
    def resetProgram(self):
        self.program = self.programBase.copy()
        self.pc = 0
        self.inputBuffer = []
        self.outputBuffer = []
        self.finished = False

    # Push an input to the input buffer.
    def pushInput(self, input):
        self.inputBuffer.extend(input)

    # Pop an input fron the input buffer.
    def popInput(self):
        if len(self.inputBuffer) > 0:
            return self.inputBuffer.pop(0)
        
        return None
    
    # Print the output buffer.
    def printOutput(self):
        for output in self.outputBuffer:
            print(output)

    # Runs the program.
    def runProgram(self):

        while True:
            code = self.program[self.pc]

            # Check if the exit condition is met.
            if code == 99:
                self.finished = True
                break

            # Get the current instruction.
            match = opCodePattern.match(str(code))
            instruction = self.getInstruction(int(match[2]))
            if not instruction:
                return

            size = instruction.size()
            
            # Get the parameters for the instruction.
            paramModes = self.getParamModes(instruction.parameters, match[1])
            params = self.getParams(self.pc, paramModes)

            # Execute the instruction.
            result = instruction.execute(params)

            # Check if the instruction causes an output.
            if instruction.output:
                self.outputBuffer.append(result)

            # Check if the instruction has result.
            if instruction.result:
                o = self.program[self.pc + size - 1]
                self.program[o] = result

            # Check if the instruction modifies the program counter.
            if instruction.jumps and result:
                self.pc = result
            else:
                self.pc += size

    # Gets an instruction from a given opcode.
    def getInstruction(self, code):
        if code == 1:
            return Add()

        if code == 2:
            return Multiply()

        if code == 3:
            input = self.popInput()
            if input == None:
                return None

            return Input(input)
            
        if code == 4:
            return Output()

        if code == 5:
            return JumpIfTrue()
        
        if code == 6:
            return JumpIfFalse()
        
        if code == 7:
            return LessThan()

        if code == 8:
            return Equals()
    
    # Gets a list of paramater modes.
    def getParamModes(self, paramCount, paramModeString):
        parameterModes = [0] * paramCount

        if paramModeString:

            paramModeStrings = list(paramModeString)
            paramModeStrings.reverse()

            for i, mode in enumerate(paramModeStrings):
                parameterModes[i] = int(mode)

        return parameterModes
    
    # Gets a list of parameter values.
    def getParams(self, pc, paramModes):
        params = []
        offset = pc + 1

        for mode in paramModes:

            if mode == 1:
                params.append(self.program[offset])
            else:
                params.append(self.program[self.program[offset]])

            offset += 1

        return params
