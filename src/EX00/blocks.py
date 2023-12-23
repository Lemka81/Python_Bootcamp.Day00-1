import sys


def error_msg() -> None:
    print("ERROR.\nUsage: cat data_hashes.txt| python blocks.py 10")


if len(sys.argv) != 2:
    error_msg()
else:
    blocks_nbr: str = sys.argv[1]
    if blocks_nbr.isdigit() and 0 <= int(blocks_nbr) <= 10:
        for _ in range(int(blocks_nbr)):
            block: str = input()
            if len(block) == 32 and block.startswith("00000") and block[5] != "0":
                print(block)
    else:
        error_msg()
