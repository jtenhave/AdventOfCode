import re

opCodePattern = re.compile("(\d*?)(\d{1,2})$")

# A class that represents an instruction for the Intcode computer. 
class Instruction: 
    def __init__(self):
        self.parameters = 0
        self.output = True
        self.jumps = False

    # Returns the size of the instruction.
    def size(self):
        return 1 + self.parameters + (1 if self.output else 0)

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
    def __init__(self):
        super().__init__()
        self.parameters = 0
    
    # Executes the instruction.
    def execute(self, params):
        return int(input("Enter Value:\n")) 

# A class that represents an Output instruction for the Intcode computer.
class Output(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 1
        self.output = False

    # Executes the instruction.
    def execute(self, params):
        return print(params[0])

# A class that represents a Jump-If-True instruction for the Intcode computer.
class JumpIfTrue(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.output = False
        self.jumps = True;

    # Executes the instruction.
    def execute(self, params):
        return params[1] if params[0] != 0 else None

# A class that represents a Jump-If-False instruction for the Intcode computer.
class JumpIfFalse(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.output = False
        self.jumps = True;

    # Executes the instruction.
    def execute(self, params):
        return params[1] if params[0] == 0 else None

# A class that represents a Less-Than instruction for the Intcode computer.
class LessThan(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.output = True

    # Executes the instruction.
    def execute(self, params):
        return 1 if params[0] < params[1] else 0

# A class that represents an Equals instruction for the Intcode computer.
class Equals(Instruction):
    def __init__(self):
        super().__init__()
        self.parameters = 2
        self.output = True

    # Executes the instruction.
    def execute(self, params):
        return 1 if params[0] == params[1] else 0

# A class that represents an Intcode computer.
class Computer:

    # Load a program into the computer.
    def loadProgram(self, program):

        self.programBase = {}

        for i, v in enumerate(program.split(",")):
            self.programBase[i] = int(v)

        self.program = self.programBase.copy()

    # Resets the program to the loaded state.
    def resetProgram(self):
        self.program = self.programBase.copy()

    # Runs the program.
    def runProgram(self):
        pc = 0;
        code = self.program[pc]

        # Check if the program should exit.
        while code != 99:
            
            # Get the current instruction.
            match = opCodePattern.match(str(code))
            instruction = self.getInstruction(int(match[2]))
            size = instruction.size()
            
            # Get the parameters for the initial instruction.
            paramModes = self.getParamModes(instruction.parameters, match[1])
            params = self.getParams(pc, paramModes)

            # Execute the instruction.
            output = instruction.execute(params)
            
            # Check if the instruction has output.
            if instruction.output:
                o = self.program[pc + size - 1]
                self.program[o] = output

            # Check if the instruction modifies the program counter.
            if instruction.jumps and output:
                pc = output
            else:
                pc += size

            code = self.program[pc]

    # Gets an instruction from a given opcode.
    def getInstruction(self, code):
        if code == 1:
            return Add()

        if code == 2:
            return Multiply()

        if code == 3: 
            return Input()
            
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
        paramModes = [0] * paramCount

        if paramModeString:

            paramModeStrings = list(paramModeString)
            paramModeStrings.reverse()

            for i, mode in enumerate(paramModeStrings):
                paramModes[i] = int(mode)

        return paramModes
    
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
