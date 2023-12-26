import sys


def error_msg() -> None:
    print('ERROR. \nUsage: python decypher.py "Some random text"')


def get_decypher():
    cypher: list[str] = sys.argv[1].split()
    for word in cypher:
        print(word[0], end="")
    print()


if len(sys.argv) < 2:
    error_msg()
else:
    get_decypher()
