import sys

ARGS: list = sys.argv[1:]

total_lines = 0
total_words = 0
total_characters = 0

if len(ARGS) > 0:
    for file_name in ARGS:
        with open(file_name) as file:
            lines = file.readlines()

        w = 0
        c = 0
        for line in lines:
            w += len(line.split())
            c += len(line)

        total_lines += len(lines)
        total_words += w
        total_characters += c

        s = '{:8d}'.format(len(lines)) + " " + \
            '{:8d}'.format(w) + " " + \
            '{:8d}'.format(c) + " " + file_name
        print(s)

    if len(sys.argv) > 2:
        s = '{:8d}'.format(total_lines) + " " + \
            '{:8d}'.format(total_words) + " " + \
            '{:8d}'.format(total_characters) + " total"
        print(s)

else:
    w = 0
    c = 0
    l = 0
    for line in sys.stdin:
        w += len(line.split())
        c += len(line)
        l += 1

    s = '{:8d}'.format(l) + " " + \
        '{:8d}'.format(w) + " " + \
        '{:8d}'.format(c)
    print(s)