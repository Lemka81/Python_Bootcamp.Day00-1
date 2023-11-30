import sys

def valid():
	if len(sys.argv) == 2:
		return 1
	else:
		return None

def make_abbreviation():
    splitted_string = sys.argv[1].split()
    abbreviation = ""
    for word in splitted_string:
        abbreviation += word[0]
    return (abbreviation)


def main():
    if valid():
        code_word = make_abbreviation()
        print(code_word)
    else:
        print("ERROR: Wrong arguments!!! \nUsage:")
        print("python decypher.py \"Some random words\"")

if __name__ == "__main__":
    main()