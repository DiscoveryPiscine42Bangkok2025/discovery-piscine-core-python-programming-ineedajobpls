import sys


def downcase_all(s):
    return s.lower()
if len(sys.argv) <=1:
    print("none")
else:
    arguments =  " ".join(sys.argv[1:])
    print(downcase_all(arguments))
