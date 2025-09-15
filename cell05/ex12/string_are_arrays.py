#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    if 'z' in input_string:
        print('z' * input_string.count('z'))
    else:
        print("none")
