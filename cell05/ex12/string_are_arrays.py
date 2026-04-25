import sys

if len(sys.argv) != 2:
    print('none')
    sys.exit(0)

input_string = sys.argv[1]

c = input_string.count('z')
if c == 0:
    print('none')
else:
    print('z' * c)