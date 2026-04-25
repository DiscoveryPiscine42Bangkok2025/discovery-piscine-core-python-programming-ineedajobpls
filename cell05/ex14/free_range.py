import sys

if len(sys.argv) != 3:
    print('none')
    sys.exit(0)
 
n = int(sys.argv[1])
m=  int(sys.argv[2])

if n <= m:
    r = list(range(n, m + 1))
else:
    r = list(range(n, m - 1, -1))

print (r)