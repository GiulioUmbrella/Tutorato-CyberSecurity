#!/usr/bin/python3

import sys

def hello_user(name):
    print(f"Hello {name}!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} string")
        exit()

    hello_user(sys.argv[1])