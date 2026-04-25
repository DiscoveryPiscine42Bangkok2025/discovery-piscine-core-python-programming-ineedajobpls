import sys
import re

if len(sys.argv) != 3:
    print('none')
    sys.exit()

keyword = sys.argv[1]
search = sys.argv[2]
 
matches = re.findall((re.escape)(keyword),search)

if not matches or not keyword:
    print('none')
else:
    print(len(matches)) 
