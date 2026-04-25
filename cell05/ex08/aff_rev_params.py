import sys
n = sys.argv[1:]

if len(sys.argv) <3:
    print('none')
else:
    for n in reversed(n):
        print(n)