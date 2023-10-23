#!/usr/bin/python3
from string import ascii_uppercase
from string import ascii_lowercase
from string import digits

B64_SYMBOLS = ascii_uppercase + ascii_lowercase + digits + '+/'

def print_block(i):
    print(f"{i:>3} {bin(i)[2:]:0>6} {B64_SYMBOLS[i]:>4}|",end=' ')

def print_b64_table():
    print("IDX    BIN  CHR| "*4)
    for i in range(16):
        print_block(i)
        print_block(i+16)
        print_block(i+32)
        print_block(i+48)
        print()

print_b64_table()
