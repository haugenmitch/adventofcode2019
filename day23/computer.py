class Computer:

    def __init__(self, program, inputs=[]):
        if type(program) == str:
            with open(program) as f:
                program = [int(n) for n in f.read().strip().split(',')]
        self.__program = {}
        for i, val in enumerate(program):
            self.__program[i] = val
        self.__pc = 0
        self.__base = 0
        self.__inputs = inputs
        self.__outputs = []
        self.__out = False
        self.__clear()

    def run(self):
        self.__clear()
        while True:
            if self.__pc not in self.__program:
                print('Error: invalid program position')
                return
            instruction = self.__decode_instruction(self.__get(self.__pc))
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

    def __set(self, index, mode, val):
        if mode == 0:
            self.__program[index] = val
        elif mode == 2:
            self.__program[self.__base + index] = val
        else:
            print('Error: unknown setting mode')

    def __get(self, index):
        if index not in self.__program:
            return 0
        else:
            return self.__program[index]

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
        elif opcode in [3, 4, 9]:
            return 1
        else:
            return 0

    def __execute(self, opcode, modes):
        if opcode == 1:
            self.__add(modes)
        elif opcode == 2:
            self.__multiply(modes)
        elif opcode == 3:
            self.__take_input(modes)
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
        elif opcode == 9:
            self.__set_relative_base(modes)
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
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        self.__set(self.__get(self.__pc + 3), modes[2], val1 + val2)
        self.__pc = self.__pc + 4

    def __multiply(self, modes):
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        self.__set(self.__get(self.__pc + 3), modes[2], val1 * val2)
        self.__pc = self.__pc + 4

    def __take_input(self, modes):
        if len(self.__inputs) > 0:
            self.__set(self.__get(self.__pc + 1), modes[0], self.__inputs.pop(0))
            self.__pc = self.__pc + 2
        else:
            self.__in = True

    def __output(self, modes):
        self.__outputs.append(self.__get_arg(1, modes[0]))
        self.__pc = self.__pc + 2
        self.__out = True

    def __jump_if_true(self, modes):
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        if val1:
            self.__pc = val2
        else:
            self.__pc = self.__pc + 3

    def __jump_if_false(self, modes):
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        if not val1:
            self.__pc = val2
        else:
            self.__pc = self.__pc + 3

    def __less_than(self, modes):
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        self.__set(self.__get(self.__pc + 3), modes[2], 1 if val1 < val2 else 0)
        self.__pc = self.__pc + 4

    def __equal_to(self, modes):
        val1 = self.__get_arg(1, modes[0])
        val2 = self.__get_arg(2, modes[1])
        self.__set(self.__get(self.__pc + 3), modes[2], 1 if val1 == val2 else 0)
        self.__pc = self.__pc + 4

    def __set_relative_base(self, modes):
        self.__base = self.__base + self.__get_arg(1, modes[0])
        self.__pc = self.__pc + 2

    def __quit(self):
        self.__pc = len(self.__program)  # moves the pc to the end of the program
        self.__halt = True

    def __unknown(self, opcode, modes):
        print('Unknown opcode (pc/opcode/modes): ' + str(self.__pc) + ' / ' + str(opcode) + ' / ' + str(modes))
        self.__pc = len(self.__program)  # moves the pc to the end of the program
        self.__err = True

    def __get_arg(self, arg_num, mode):
        if mode == 0:
            return self.__get(self.__get(self.__pc + arg_num))
        elif mode == 1:
            return self.__get(self.__pc + arg_num)
        elif mode == 2:
            return self.__get(self.__base + self.__get(self.__pc + arg_num))
        else:
            print('Error: Invalid mode')
            exit()
