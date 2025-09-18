#!/usr/bin/env python3

import sys
from checkmate import checkmate, generate_threat_map

def read_board_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def main():
    if len(sys.argv) < 2:
        print("Error$")
        return

    option = None
    if sys.argv[1].startswith("--"):
        option = sys.argv[1]
        files = sys.argv[2:]
    else:
        files = sys.argv[1:]

    for filename in files:
        board = read_board_from_file(filename)
        if board is None:
            print(f"Error reading {filename}")
            continue

        print(f"Processing board from {filename}:")
        print(board)

        if option == "--threat-map":
            print("Generating threat map...")
            print(generate_threat_map(board))  # จะเห็นผลลัพธ์นี้หรือไม่
        else:
            checkmate(board)

if __name__ == "__main__":
    main()
