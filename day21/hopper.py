from computer import Computer

c = Computer('program.txt')
c.run()
print(''.join([chr(char) for char in c.output()]))

c.input([ord(c) for c in 'NOT C J\nAND D J\nNOT A T\nOR T J\nWALK\n'])
c.run()
print(''.join([chr(val) if val < 256 else str(val) for val in c.output()]))
