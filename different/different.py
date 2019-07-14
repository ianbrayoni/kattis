"""
https://open.kattis.com/problems/different

In Python3, plain `int` type is unbounded but in other
languages like c/c++ one may need to be careful of long long.

If you need to check for the machine's word size, that's still
available in Python 3 as `sys.maxsize`

python different/different.py < different/data/sample.in
"""
import sys


def difference(num1, num2):
    return abs(num1 - num2)


if __name__ == "__main__":
    num_pairs = (n.split() for n in sys.stdin.readlines())
    for num_pair in num_pairs:
        num1, num2 = num_pair
        print(difference(int(num1), int(num2)))
