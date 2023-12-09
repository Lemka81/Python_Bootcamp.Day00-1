import sys

def valid():
	if len(sys.argv) == 2:
		return 1
	else:
		return None

if valid():
    line = sys.argv[1].split()
    for item in line:
        print(item[0], end='')
    print()
else:
    print("ERROR: Wrong arguments!!! \nUsage:")
    print("python decypher.py \"Some random text\"")
