class Computer:

    def __init__(self, program, inputs):
        self.__program = program
        self.__pc = 0
        self.__inputs = inputs
        self.__outputs = []
        self.__out = False
        self.__clear()

    def run(self):
        self.__clear()
        while self.__pc < len(self.__program):
            instruction = self.__decode_instruction(self.__program[self.__pc])
            if not self.__execute(instruction[0], instruction[1]):
                return

    def input(self, val):
        if type(val) == list:
            self.__inputs = self.__inputs + val
        else:
            self.__inputs.append(val)

    def output(self):
        out = self.__outputs.copy()
        self.__outputs.clear()
        self.__out = False
        return out

    def input_requested(self):
        return self.__in

    def output_ready(self):
        return self.__out

    def halted(self):
        return self.__halt

    def error(self):
        return self.__err

    def __decode_instruction(self, instruction):
        opcode = int(str(instruction)[-2:])
        modes_str = str(instruction)[-3::-1]
        modes = []
        for i in range(self.__num_params(opcode)):
            modes.append(0 if i >= len(modes_str) else int(modes_str[i]))
        return opcode, modes

    @staticmethod
    def __num_params(opcode):
        if opcode in [1, 2, 7, 8]:
            return 3
        elif opcode in [5, 6]:
            return 2
        elif opcode in [3, 4]:
            return 1
        else:
            return 0

    def __execute(self, opcode, modes):
        if opcode == 1:
            self.__add(modes)
        elif opcode == 2:
            self.__multiply(modes)
        elif opcode == 3:
            self.__take_input()
        elif opcode == 4:
            self.__output(modes)
        elif opcode == 5:
            self.__jump_if_true(modes)
        elif opcode == 6:
            self.__jump_if_false(modes)
        elif opcode == 7:
            self.__less_than(modes)
        elif opcode == 8:
            self.__equal_to(modes)
        elif opcode == 99:
            self.__quit()
        else:
            self.__unknown(opcode, modes)
        return not self.__halting()

    def __halting(self):
        return self.__err | self.__in | self.__halt

    def __clear(self):
        self.__err = False
        self.__in = False
        self.__halt = False

    def __add(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        self.__program[self.__program[self.__pc + 3]] = val1 + val2
        self.__pc = self.__pc + 4

    def __multiply(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        self.__program[self.__program[self.__pc + 3]] = val1 * val2
        self.__pc = self.__pc + 4

    def __take_input(self):
        if len(self.__inputs) > 0:
            self.__program[self.__program[self.__pc + 1]] = self.__inputs.pop(0)
            self.__pc = self.__pc + 2
        else:
            self.__in = True

    def __output(self, modes):
        self.__outputs.append(self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]])
        self.__pc = self.__pc + 2
        self.__out = True

    def __jump_if_true(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        if val1:
            self.__pc = val2
        else:
            self.__pc = self.__pc + 3

    def __jump_if_false(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        if not val1:
            self.__pc = val2
        else:
            self.__pc = self.__pc + 3

    def __less_than(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        self.__program[self.__program[self.__pc + 3]] = 1 if val1 < val2 else 0
        self.__pc = self.__pc + 4

    def __equal_to(self, modes):
        val1 = self.__program[self.__pc + 1] if modes[0] else self.__program[self.__program[self.__pc + 1]]
        val2 = self.__program[self.__pc + 2] if modes[1] else self.__program[self.__program[self.__pc + 2]]
        self.__program[self.__program[self.__pc + 3]] = 1 if val1 == val2 else 0
        self.__pc = self.__pc + 4

    def __quit(self):
        self.__pc = len(self.__program)  # moves the pc to the end of the program
        self.__halt = True

    def __unknown(self, opcode, modes):
        print('Unknown opcode (pc/opcode/modes): ' + str(self.__pc) + ' / ' + str(opcode) + ' / ' + str(modes))
        self.__pc = len(self.__program)  # moves the pc to the end of the program
        self.__err = True
