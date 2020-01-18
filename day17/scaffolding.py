import sys
from computer import Computer

c = Computer(sys.argv[1])

main = 'A,B,A,C,A,B,C,C,A,B\n'
A = 'R,8,L,10,R,8\n'
B = 'R,12,R,8,L,8,L,12\n'
C = 'L,12,L,10,L,8\n'
continuous = 'n\n'

c.input([ord(c) for c in main])
c.input([ord(c) for c in A])
c.input([ord(c) for c in B])
c.input([ord(c) for c in C])
c.input([ord(c) for c in continuous])
c.run()
print(c.output()[-1])
