
import sys



f = len(sys.argv) - 1

if f == 0:
    print('nope')
else:
    print('parameters: ' , f)
    

    for i in range(1, len(sys.argv)):
        param = sys.argv[i]
        print(param + ':' , len(param))