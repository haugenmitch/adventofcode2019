import sys
from computer import Computer

c = Computer('program.txt')
c.run()

while True:
    print(''.join([chr(n) for n in c.output()]))

    cmd = input()
    if cmd == 'exit':
        break
    cmd += '\n'
    c.input([ord(n) for n in cmd])
    c.run()

# take mutex, asterisk, space law space brochure, and food ration
