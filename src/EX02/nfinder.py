import sys

def check(line, i):
    if i > 3 or len(line) != 5:
        print("Error")
        return None
    else:
        if check_m(line, i):
            
        return 1

def check_m(line, i):
    if i == 1:
        return line[::4] == "**" and "*" not in line[1:4]
    if i == 2:
        return line[::3] == line[3:] == "**" and "*" not in line[2]
    if i == 3:
        return line[::2] == "***" and "*" not in line[1::2]

def main():
    i = 0
    res = True
    for line in sys.stdin:
        line = line.rstrip()
        if len(line):
            i += 1
            check(line, i)
                

            

if __name__ == "__main__":
    main()
