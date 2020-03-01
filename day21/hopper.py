from computer import Computer

c = Computer('program.txt')
c.run()
print(''.join([chr(char) for char in c.output()]))

c.input([ord(c) for c in 'NOT A T\nNOT B J\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT J T\nOR E T\nOR H T\nAND T J\nRUN\n'])
c.run()
print(''.join([chr(val) if val < 256 else str(val) for val in c.output()]))
