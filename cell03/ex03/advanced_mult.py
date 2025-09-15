#!/usr/bin/env python3
import sys

# เช็คว่า มี argument หรือไม่
if len(sys.argv) > 1:
    print("none")
else:
    # หากไม่มี argument แสดงตารางการคูณ
    i = 0
    while i <= 10:
        print(f"Table de {i}: ", end="")
        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1
