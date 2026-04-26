import sys

def shrink (s):
    return(s[:8])

def enlarge(s):
    return(s + 'z' * (8 - len(s)))

def check():
    for i in range(1, len(sys.argv)):
        param = sys.argv[i]
        if len(param) >= 8:
            print(shrink(param))
##        elif len(param) <= 1:
##          print('none')
        else:
            print(enlarge(param ))

if __name__ == '__main__':
    check()