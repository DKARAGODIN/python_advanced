import sys

ARGS: list = sys.argv[1:]
counter: int = 1

if len(ARGS) > 0:
    for file_name in ARGS:
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                print("{:6d}  {}".format(counter, line), end="")
                counter += 1

else:
    for line in sys.stdin:
        print("{:6d}  {}".format(counter, line), end="")
        counter += 1
