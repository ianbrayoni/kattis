"""
https://open.kattis.com/problems/romans

convert distances in English miles into Roman paces

python romans/romans.py < romans/data/t1.in
"""

import sys

ROMAN_PACES_CONST = 1000 * 5280 / 4854


def converter(miles):
    roman_paces = miles * ROMAN_PACES_CONST
    return round(roman_paces)


if __name__ == "__main__":
    miles = float(sys.stdin.readline())
    print(converter(miles))
