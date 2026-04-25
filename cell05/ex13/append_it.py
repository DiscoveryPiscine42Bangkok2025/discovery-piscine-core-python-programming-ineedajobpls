import sys

if len(sys.argv) == 1:
    print('none')
    sys.exit(0)
 
n = sys.argv[1:]

for arg in n:
    if arg.endswith('ism'):
        continue

    print(f'{arg}ism',end=' ')