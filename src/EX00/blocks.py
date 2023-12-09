import sys

def valid():
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        return 1
    else:
        return None

def valid_block(string):
    if len(string) == 32 and string[5] != "0" and string.startswith("00000"):
        return(string)

if valid():
    num_lines = int(sys.argv[1])
    if num_lines <= 10:
        input_strings = [next(sys.stdin).strip() for _ in range(num_lines)]
        
        for string in input_strings:
            block = valid_block(string)
            if block is not None:
                print(block)
else:
    print("ERROR: Wrong arguments!!! \nUsage:")			
    print("cat data_hashes_10lines.txt | python blocks.py <lines_number>")
