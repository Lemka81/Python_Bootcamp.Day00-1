import sys


def decypher() -> None:
    if len(sys.argv) == 2:
        line: list[str] = sys.argv[1].split()
        for item in line:
            print(item[0], end='')
        print()
    else:
        print("ERROR: Wrong arguments!!! \nUsage:")
        print("python decypher.py \"Some random text\"")


decypher()
