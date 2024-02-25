import sys

ARGS: list = sys.argv[1:]

def get_last_lines(file_name: str) -> list[str]:
    cache = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            cache.append(line)
            if len(cache) > 10:
                del cache[0]
    return cache


if len(ARGS) == 1:
    for line in get_last_lines(ARGS[0]):
        print(line, end="")

elif len(ARGS) > 1:
    for file_name in ARGS:
        print("==> {} <==".format(file_name))
        for line in get_last_lines(file_name):
            print(line, end="")
        print()

elif len(ARGS) == 0:
    cache = []
    for line in sys.stdin:
        cache.append(line)
        if len(cache) > 10:
            del cache[0]
    for line in cache:
        print(line, end="")
