import sys

def check_m(line, i) -> bool:
    if i == 1:
        return line[::4] == "**" and "*" not in line[1:4]
    if i == 2:
        return line[::3] == line[3:] == "**" and "*" not in line[2]
    if i == 3:
        return line[::2] == "***" and "*" not in line[1::2]

i: int = 0
for line in sys.stdin:
    line: str = line.rstrip()
    if len(line):
        i += 1
        if i > 3 or len(line) != 5:
            print("Error")
            break
        else:
            res: bool = check_m(line, i)
            if res == 0 or i == 3:
                print (res)
                break
            