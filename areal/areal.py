"""
https://open.kattis.com/problems/areal

python areal/areal.py < areal/data/1.in
"""

import sys
import math


def perimeter_pasture(square):
    side = math.sqrt(square)
    perimeter = side * 4
    return perimeter


if __name__ == "__main__":
    square = int(sys.stdin.readline())
    print(perimeter_pasture(square))
