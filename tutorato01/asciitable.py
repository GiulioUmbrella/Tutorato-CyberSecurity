#!/usr/bin/python3

def print_ascii_table_block(v):
    print(f"{v:>3}{hex(v)[2:]:>4}{chr(v):>4}|",end=' ')

def print_ascii_table():
    print("Dex Hex Chr| Dex Hex Chr| Dex Hex Chr|")
    for v1 in range(32):
        print_ascii_table_block(v1+32)
        print_ascii_table_block(v1+64)
        print_ascii_table_block(v1+96)
        print()

print_ascii_table() 